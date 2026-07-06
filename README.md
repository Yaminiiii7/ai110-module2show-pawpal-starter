# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Here is a sample terminal output from running the CLI demo script:

```text
Today's Schedule for Jordan
Daily plan for Mochi:
1. 00:00 — Feed breakfast (10 min) [priority: high] [feeding]
2. 00:10 — Feed dinner (10 min) [priority: high] [feeding]
3. 00:20 — Morning walk (30 min) [priority: high] [exercise]
4. 00:50 — Litter cleanup (15 min) [priority: medium] [care]
5. 01:05 — Playtime (20 min) [priority: medium] [enrichment]

Reasoning:
Sorted tasks by priority and fit them into 90 minutes of available time. 5 tasks were scheduled.

Planned tasks: 5
```

## 🧪 Testing PawPal+

Run the automated test suite with:

```bash
python -m pytest
```

The tests cover core behaviors such as task completion, pet task addition, chronological sorting, filtering by completion status, recurring-task creation, and conflict detection for duplicate times.

Example output:

```text
============================= test session starts =============================
platform win32 -- Python 3.10.0, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\YAMI\OneDrive\Desktop\Codepath\project2\ai110-module2show-pawpal-starter
collected 8 items

test_pawpal_system.py ....                                               [ 50%]
tests\test_pawpal.py ....                                                [100%]

============================== 8 passed in 0.05s ==============================
```

Confidence level: ⭐⭐⭐⭐☆

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Sorting behavior | Scheduler.sort_by_time() | Orders tasks by their scheduled time-of-day value in HH:MM format. |
| Filtering behavior | Scheduler.filter_tasks() | Filters tasks by pet name and completion status. |
| Conflict detection | Scheduler.detect_conflicts() | Returns lightweight warnings when tasks share the same time slot. |
| Recurring tasks | Task.mark_complete() | Creates a new task for daily or weekly recurring tasks after completion. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
