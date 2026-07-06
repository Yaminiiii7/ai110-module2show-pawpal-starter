from pawpal_system import Pet, Scheduler, Task


def test_mark_complete_updates_task_status():
    task = Task("Morning walk", 30, "high")
    assert task.is_complete is False

    task.mark_complete()

    assert task.is_complete is True


def test_adding_task_increases_pet_task_count():
    pet = Pet("Mochi", "dog")
    initial_count = len(pet.list_tasks())

    pet.add_task(Task("Feed breakfast", 10, "high"))

    assert len(pet.list_tasks()) == initial_count + 1


def test_scheduler_can_sort_filter_and_detect_conflicts():
    pet = Pet("Mochi", "dog")
    scheduler = Scheduler(pet, None, 60)

    walk = Task("Morning walk", 30, "high", time_of_day="09:00")
    feed = Task("Feed breakfast", 10, "medium", time_of_day="08:00")
    brush = Task("Brush fur", 15, "low", time_of_day="08:00")
    walk.pet_name = pet.name
    feed.pet_name = pet.name
    brush.pet_name = pet.name
    walk.is_complete = True

    sorted_tasks = scheduler.sort_by_time([walk, feed, brush])
    filtered_tasks = scheduler.filter_tasks([walk, feed, brush], completed=False)
    conflicts = scheduler.detect_conflicts([feed, brush])

    assert [task.title for task in sorted_tasks[:2]] == ["Feed breakfast", "Brush fur"]
    assert len(filtered_tasks) == 2
    assert len(conflicts) == 1


def test_recurring_task_creates_next_occurrence():
    task = Task("Water plants", 5, "medium", frequency="daily", time_of_day="07:00")

    next_task = task.mark_complete()

    assert task.is_complete is True
    assert next_task is not None
    assert next_task.frequency == "daily"
    assert next_task.is_complete is False
