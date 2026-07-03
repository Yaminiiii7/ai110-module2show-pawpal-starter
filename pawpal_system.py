"""
PawPal+ System Classes
Classes for managing pet care planning and scheduling.
"""

from datetime import datetime
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
    
    def get_available_time(self) -> int:
        """
        Calculate total available time in hours.
        
        Returns:
            Number of hours available
        """
        pass
    
    def get_preferences(self) -> List[str]:
        """
        Get owner preferences.
        
        Returns:
            List of preference strings
        """
        pass
    
    def update_info(self, name: str, start_time: int, end_time: int) -> None:
        """
        Update owner information.
        
        Args:
            name: New name
            start_time: New available start hour
            end_time: New available end hour
        """
        pass


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
        self.tasks = []
    
    def get_info(self) -> str:
        """
        Get pet information summary.
        
        Returns:
            Formatted string with pet details
        """
        pass
    
    def add_task(self, task: 'Task') -> None:
        """
        Add a task to the pet's task list.
        
        Args:
            task: Task object to add
        """
        pass
    
    def remove_task(self, task_id: int) -> None:
        """
        Remove a task by ID.
        
        Args:
            task_id: ID of task to remove
        """
        pass
    
    def list_tasks(self) -> List['Task']:
        """
        Get all tasks for this pet.
        
        Returns:
            List of Task objects
        """
        pass
    
    def get_species(self) -> str:
        """
        Get the pet's species.
        
        Returns:
            Species type
        """
        pass


class Task:
    """Represents a pet care task with duration and priority."""
    
    _id_counter = 1  # Class variable for auto-incrementing IDs
    
    def __init__(self, title: str, duration_minutes: int, priority: str, category: Optional[str] = None):
        """
        Initialize a Task.
        
        Args:
            title: Task name (e.g., "Morning walk")
            duration_minutes: How long the task takes
            priority: Priority level ("low", "medium", "high")
            category: Task category (optional)
        """
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.category = category
        self.description = ""
        self.is_recurring = False
    
    def get_duration(self) -> int:
        """
        Get task duration in minutes.
        
        Returns:
            Duration in minutes
        """
        pass
    
    def get_priority_level(self) -> int:
        """
        Convert priority to numeric level for sorting.
        
        Returns:
            Numeric priority (1=low, 2=medium, 3=high)
        """
        pass
    
    def to_string(self) -> str:
        """
        Get formatted task description.
        
        Returns:
            Formatted string representation
        """
        pass
    
    def is_high_priority(self) -> bool:
        """
        Check if task is high priority.
        
        Returns:
            True if priority is "high"
        """
        pass


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
    
    def generate_schedule(self, tasks: List[Task], owner: Owner) -> None:
        """
        Generate an optimized daily schedule.
        
        Args:
            tasks: List of tasks to schedule
            owner: Owner object with constraints
        """
        pass
    
    def sort_tasks_by_priority(self, tasks: List[Task]) -> List[Task]:
        """
        Sort tasks by priority (high to low).
        
        Args:
            tasks: List of tasks to sort
            
        Returns:
            Sorted list of tasks
        """
        pass
    
    def check_time_conflicts(self, scheduled_tasks: List[tuple]) -> bool:
        """
        Check if any scheduled tasks overlap in time.
        
        Args:
            scheduled_tasks: List of (Task, start_time) tuples
            
        Returns:
            True if conflicts found, False otherwise
        """
        pass
    
    def fit_tasks_in_available_time(self, tasks: List[Task], available_minutes: int) -> List[Task]:
        """
        Filter tasks that can fit in available time.
        
        Args:
            tasks: List of tasks to filter
            available_minutes: Available time in minutes
            
        Returns:
            List of tasks that fit
        """
        pass
    
    def display_plan(self) -> str:
        """
        Get formatted daily plan for display.
        
        Returns:
            Formatted schedule string
        """
        pass
    
    def get_reasoning(self) -> str:
        """
        Get explanation of scheduling decisions.
        
        Returns:
            Reasoning text
        """
        pass
    
    def is_schedule_valid(self) -> bool:
        """
        Verify schedule is valid (no conflicts, within time limits).
        
        Returns:
            True if schedule is valid
        """
        pass
