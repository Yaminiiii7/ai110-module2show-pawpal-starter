# PawPal+ Project Reflection

## 1. System Design

    When users first open PawPal+, they tell the app about themselves and their pet. They enter their name, their pet's name, what kind of animal they have, and any preferences they might have.

    Users then add the different tasks their pet needs throughout the day—things like morning walks, feeding times, medication, playtime, or grooming. For each task, they specify how long it takes (in minutes) and how important it is (low, medium, or high priority). They can add as many tasks as they need.
    
    Once the user has entered their tasks, they can ask the app to generate a schedule for the day. The app then smartly organizes all the tasks into a realistic plan that respects time constraints and priorities. It shows the user when each task should happen and explains why it made those choices. 

**a. Initial design**

My initial UML design includes four core classes:

1. **Owner** — Represents the pet owner with basic info and constraints
   - Attributes: name, available_hours_start, available_hours_end, preferences
   - Responsibilities: Track owner availability and preferences; provide methods to query available time and update owner info

2. **Pet** — Represents the pet being cared for
   - Attributes: name, species, age, breed, special_needs, tasks (list)
   - Responsibilities: Store pet information; manage a list of tasks; provide pet details for the schedule

3. **Task** — Represents a single pet care activity
   - Attributes: id, title, duration_minutes, priority, category, description, is_recurring
   - Responsibilities: Store task details (what needs to be done, how long, how important); provide methods to query priority level and check if it's urgent

4. **Schedule** — Orchestrates the daily plan (the "brain" of the system)
   - Attributes: pet, date, scheduled_tasks, total_available_time, total_time_used, reasoning
   - Responsibilities: Generate an optimized daily schedule by sorting and filtering tasks; check for time conflicts; ensure the plan fits within available time; explain the scheduling decisions to the user

The relationships are: Owner owns Pet(s), Pet has Task(s), and Schedule plans for a Pet by organizing its Task(s).

The Schedule class is the most complex—it coordinates with Owner and Task to produce an intelligent plan that respects priorities and time constraints.

**b. Design changes**

No significant design changes at this stage. The class skeleton I created aligns with the initial UML design.

However, I anticipate potential design changes during implementation:

**Possible change 1: Add a ScheduledTask class**
- Initially, I planned to store `scheduled_tasks` as tuples of (Task, start_time) in the Schedule class.
- During implementation, I may extract this into a separate `ScheduledTask` class with attributes like task_id, start_time, and end_time. This would make the code cleaner and easier to work with.
- Reason: It's more maintainable and provides a dedicated place to add methods like `check_overlap()` or `get_duration()`.

**Possible change 2: Separate priority handling from Task**
- I might create a `PriorityLevel` enum instead of using strings ("low", "medium", "high").
- Reason: This prevents invalid priority values and makes sorting logic more reliable.

**Possible change 3: Add a TimeSlot or AvailableHours class**
- Currently, Owner stores `available_hours_start` and `available_hours_end` as separate integers.
- I might refactor this into a dedicated class to make time constraints more explicit and reusable.
- Reason: This makes the code clearer about what "available time" means and makes it easier to handle edge cases like tasks spanning midnight.

I'll decide on these changes as I implement the scheduling logic and discover what feels most natural in Python.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- The scheduler currently checks for exact time matches when detecting conflicts instead of comparing full overlapping intervals.
- This tradeoff is reasonable for this project because the app is focused on lightweight daily planning, and exact-time conflict checks are simple, readable, and easy to explain to a pet owner.

---

## 3. AI Collaboration

**a. How you used AI**

- I used AI throughout the project for brainstorming the class design, generating the initial Python implementation, debugging the scheduler logic, and drafting tests.
- The most helpful prompts were specific and focused, such as asking how the Scheduler should retrieve tasks from an Owner, how to structure recurring-task logic, and how to make the Streamlit UI reflect the backend features.

**b. Judgment and verification**

- I did not accept every AI suggestion as-is. For example, I adjusted an early draft of the recurring-task logic so it stayed simple and readable instead of adding overly abstract date handling.
- I verified AI suggestions by running the CLI demo and the pytest suite so the final code was based on working behavior rather than just plausible ideas.

---

## 4. Testing and Verification

**a. What you tested**

- I tested task completion behavior, pet task collection, chronological sorting, filtering by completion status, recurring-task creation, and conflict detection.
- These tests matter because they cover the scheduling rules that most directly affect whether the app produces a useful daily plan.

**b. Confidence**

- I am confident that the core scheduling flow works for the planned scenarios because it is supported by automated tests and a working CLI demo.
- If I had more time, I would test edge cases such as overlapping task durations, very large task lists, and tasks with missing or inconsistent time values.

---

## 5. Reflection

**a. What went well**

- I am most satisfied with how the system moved from a simple class skeleton into a working scheduler that the UI and tests both use.

**b. What you would improve**

- I would improve the scheduling model by adding more realistic overlap handling and a more detailed time-slot representation.

**c. Key takeaway**

- A useful lesson from this project is that clear object relationships make it much easier to connect the backend logic to both a CLI demo and a user-facing app.
