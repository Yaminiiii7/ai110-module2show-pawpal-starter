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

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
