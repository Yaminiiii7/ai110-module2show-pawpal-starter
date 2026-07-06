"""
PawPal+ System Classes
Classes for managing pet care planning and scheduling.
"""

from datetime import datetime, timedelta
from typing import List, Optional


class Owner:
    """Represents a pet owner with availability and preferences."""

    def __init__(self, name: str, available_hours_start: int, available_hours_end: int):
        """
        Initialize an Owner.

        Args:
            name: Owner's name
            available_hours_start: Hour when owner becomes available (0-23)
            available_hours_end: Hour when owner stops being available (0-23)
        """
        self.name = name
        self.available_hours_start = available_hours_start
        self.available_hours_end = available_hours_end
        self.preferences = []
        self.pets: List["Pet"] = []

    def get_available_time(self) -> int:
        """Return the owner's available hours as a simple duration."""
        return max(0, self.available_hours_end - self.available_hours_start)

    def get_preferences(self) -> List[str]:
        """Return the owner's saved preferences as a list."""
        return list(self.preferences)

    def update_info(self, name: str, start_time: int, end_time: int) -> None:
        """Update the owner's basic scheduling information."""
        self.name = name
        self.available_hours_start = start_time
        self.available_hours_end = end_time

    def add_pet(self, pet: "Pet") -> None:
        """Add a pet to the owner's household."""
        if pet not in self.pets:
            self.pets.append(pet)

    def get_all_tasks(self) -> List["Task"]:
        """Collect all tasks from every pet managed by the owner."""
        tasks: List["Task"] = []
        for pet in self.pets:
            tasks.extend(pet.list_tasks())
        return tasks


class Pet:
    """Represents a pet that needs care tasks."""

    def __init__(self, name: str, species: str, age: Optional[int] = None, breed: Optional[str] = None):
        """
        Initialize a Pet.

        Args:
            name: Pet's name
            species: Type of animal (dog, cat, other)
            age: Pet's age (optional)
            breed: Pet's breed (optional)
        """
        self.name = name
        self.species = species
        self.age = age
        self.breed = breed
        self.special_needs = []
        self.tasks: List["Task"] = []

    def get_info(self) -> str:
        """Return a readable summary of the pet's basic details."""
        details = [self.name, self.species]
        if self.age is not None:
            details.append(f"age {self.age}")
        if self.breed:
            details.append(self.breed)
        if self.special_needs:
            details.append(f"needs: {', '.join(self.special_needs)}")
        return " | ".join(details)

    def add_task(self, task: "Task") -> None:
        """
        Add a task to the pet's task list.

        Args:
            task: Task object to add
        """
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task_id: int) -> None:
        """Remove a task from the pet by its ID."""
        self.tasks = [task for task in self.tasks if task.id != task_id]

    def list_tasks(self) -> List["Task"]:
        """Return a copy of the pet's task list."""
        return list(self.tasks)

    def get_species(self) -> str:
        """Return the pet's species."""
        return self.species


class Task:
    """Represents a pet care task with duration and priority."""

    _id_counter = 1  # Class variable for auto-incrementing IDs

    def __init__(
        self,
        title: str,
        duration_minutes: int,
        priority: str,
        category: Optional[str] = None,
        frequency: Optional[str] = None,
        time_of_day: Optional[str] = None,
    ):
        """Initialize a task with optional timing and recurrence metadata."""
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority.lower()
        self.category = category
        self.description = ""
        self.is_recurring = bool(frequency)
        self.is_complete = False
        self.frequency = frequency.lower() if frequency else "once"
        self.time_of_day = time_of_day
        self.pet_name: Optional[str] = None

    def get_duration(self) -> int:
        """Return the task duration in minutes."""
        return self.duration_minutes

    def get_priority_level(self) -> int:
        """Return a numeric priority used for sorting tasks."""
        levels = {"low": 1, "medium": 2, "high": 3}
        return levels.get(self.priority, 2)

    def to_string(self) -> str:
        """Return a readable summary of the task."""
        category_text = f" [{self.category}]" if self.category else ""
        return f"{self.title} ({self.duration_minutes} min) [priority: {self.priority}]" + category_text

    def is_high_priority(self) -> bool:
        """Return True when the task has high priority."""
        return self.priority == "high"

    def mark_complete(self) -> Optional["Task"]:
        """Mark the task as completed and return a new recurring task when needed."""
        self.is_complete = True
        if self.frequency in {"daily", "weekly"}:
            next_task = Task(
                self.title,
                self.duration_minutes,
                self.priority,
                category=self.category,
                frequency=self.frequency,
                time_of_day=self.time_of_day,
            )
            next_task.pet_name = self.pet_name
            if self.frequency == "daily":
                next_task.description = f"Next occurrence for {self.title}"
            return next_task
        return None


class Schedule:
    """Represents a daily pet care schedule."""

    def __init__(self, pet: Pet, date: datetime, available_minutes: int):
        """
        Initialize a Schedule.

        Args:
            pet: Pet object this schedule is for
            date: Date of the schedule
            available_minutes: Total minutes available for tasks
        """
        self.pet = pet
        self.date = date
        self.scheduled_tasks = []  # List of tuples: (Task, start_time)
        self.total_available_time = available_minutes
        self.total_time_used = 0
        self.reasoning = ""

    def generate_schedule(self, tasks: List[Task], owner: Optional[Owner]) -> None:
        """
        Generate an optimized daily schedule.

        Args:
            tasks: List of tasks to schedule
            owner: Owner object with constraints
        """
        if tasks:
            candidate_tasks = list(tasks)
        elif owner is not None:
            candidate_tasks = owner.get_all_tasks()
        else:
            candidate_tasks = []

        available_minutes = self.total_available_time
        if available_minutes <= 0 and owner is not None:
            available_minutes = max(0, (owner.available_hours_end - owner.available_hours_start) * 60)

        sorted_tasks = self.sort_tasks_by_priority(candidate_tasks)
        fit_tasks = self.fit_tasks_in_available_time(sorted_tasks, available_minutes)

        scheduled_tasks = []
        used_time = 0
        start_time = 0

        for task in fit_tasks:
            task_duration = task.get_duration()
            if used_time + task_duration > available_minutes:
                continue
            scheduled_tasks.append((task, start_time))
            used_time += task_duration
            start_time += task_duration

        self.scheduled_tasks = scheduled_tasks
        self.total_time_used = used_time
        self.reasoning = (
            f"Sorted tasks by priority and fit them into {available_minutes} minutes of available time. "
            f"{len(scheduled_tasks)} tasks were scheduled."
        )

    def sort_tasks_by_priority(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by priority (high to low)."""
        return sorted(tasks, key=lambda task: (-task.get_priority_level(), task.get_duration()))

    def sort_by_time(self, tasks: List[Task]) -> List[Task]:
        """Sort tasks by their scheduled time of day, using HH:MM values."""
        return sorted(tasks, key=lambda task: task.time_of_day or "23:59")

    def filter_tasks(self, tasks: List[Task], pet_name: Optional[str] = None, completed: Optional[bool] = None) -> List[Task]:
        """Filter tasks by pet name and completion state."""
        filtered_tasks = []
        for task in tasks:
            if pet_name is not None and task.pet_name != pet_name:
                continue
            if completed is not None and task.is_complete != completed:
                continue
            filtered_tasks.append(task)
        return filtered_tasks

    def detect_conflicts(self, tasks: List[Task]) -> List[str]:
        """Return simple warnings when two tasks share the same time slot."""
        warnings = []
        seen = {}
        for task in tasks:
            key = task.time_of_day or "00:00"
            if key in seen:
                warnings.append(f"Conflict: {seen[key].title} and {task.title} both occur at {key}.")
            else:
                seen[key] = task
        return warnings

    def check_time_conflicts(self, scheduled_tasks: List[tuple]) -> bool:
        """
        Check if any scheduled tasks overlap in time.

        Args:
            scheduled_tasks: List of (Task, start_time) tuples

        Returns:
            True if conflicts found, False otherwise
        """
        for index, (task, start_time) in enumerate(scheduled_tasks):
            task_end = start_time + task.get_duration()
            for other_task, other_start in scheduled_tasks[index + 1 :]:
                other_end = other_start + other_task.get_duration()
                if start_time < other_end and other_start < task_end:
                    return True
        return False

    def fit_tasks_in_available_time(self, tasks: List[Task], available_minutes: int) -> List[Task]:
        """
        Filter tasks that can fit in available time.

        Args:
            tasks: List of tasks to filter
            available_minutes: Available time in minutes

        Returns:
            List of tasks that fit
        """
        fitted_tasks = []
        used_time = 0
        for task in tasks:
            if used_time + task.get_duration() <= available_minutes:
                fitted_tasks.append(task)
                used_time += task.get_duration()
        return fitted_tasks

    @staticmethod
    def _format_time(minutes: int) -> str:
        """Convert minute counts into a readable HH:MM time string."""
        hours, mins = divmod(minutes, 60)
        return f"{hours:02d}:{mins:02d}"

    def display_plan(self) -> str:
        """
        Get formatted daily plan for display.

        Returns:
            Formatted schedule string
        """
        if not self.scheduled_tasks:
            return "No tasks scheduled."

        lines = [f"Daily plan for {self.pet.name if self.pet else 'your pet'}:"]
        for index, (task, start_time) in enumerate(self.scheduled_tasks, start=1):
            lines.append(f"{index}. {self._format_time(start_time)} — {task.to_string()}")
        return "\n".join(lines)

    def get_reasoning(self) -> str:
        """
        Get explanation of scheduling decisions.

        Returns:
            Reasoning text
        """
        return self.reasoning

    def is_schedule_valid(self) -> bool:
        """
        Verify schedule is valid (no conflicts, within time limits).

        Returns:
            True if schedule is valid
        """
        if self.check_time_conflicts(self.scheduled_tasks):
            return False
        if self.total_time_used > self.total_available_time:
            return False
        return True


class Scheduler(Schedule):
    """Brain that retrieves, organizes, and manages tasks across pets."""

    def get_tasks_from_owner(self, owner: Owner) -> List[Task]:
        """Collect tasks from every pet owned by the owner."""
        return owner.get_all_tasks()

    def build_plan_for_owner(self, owner: Owner, available_minutes: Optional[int] = None) -> List[Task]:
        """Create a prioritized task plan for the owner's pets."""
        if available_minutes is not None:
            self.total_available_time = available_minutes

        tasks = self.get_tasks_from_owner(owner)
        self.generate_schedule(tasks, owner)
        return [task for task, _ in self.scheduled_tasks]

    def add_pet_to_owner(self, owner: Owner, pet: Pet) -> None:
        """Register a pet with the owner so the scheduler can see it."""
        owner.add_pet(pet)

    def summarize_tasks(self, owner: Owner) -> str:
        """Provide a short summary of all tasks the scheduler can see."""
        tasks = self.get_tasks_from_owner(owner)
        if not tasks:
            return "No tasks available."
        return "; ".join(task.to_string() for task in tasks)
