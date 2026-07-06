import pytest

from pawpal_system import Owner, Pet, Task, Schedule


def make_owner_and_pet():
    owner = Owner("Jordan", 7, 20)
    pet = Pet("Mochi", "dog")
    owner.pets = [pet]
    return owner, pet


def test_task_priority_and_string():
    task = Task("Morning walk", 30, "high", "exercise")
    assert task.get_duration() == 30
    assert task.get_priority_level() == 3
    assert task.is_high_priority() is True
    assert "Morning walk" in task.to_string()


def test_pet_manages_tasks():
    pet = Pet("Mochi", "dog")
    task = Task("Feed", 10, "medium")
    pet.add_task(task)
    assert pet.list_tasks() == [task]
    pet.remove_task(task.id)
    assert pet.list_tasks() == []


def test_owner_reports_available_time_and_preferences():
    owner = Owner("Jordan", 7, 20)
    owner.preferences = ["quiet", "morning walks"]
    assert owner.get_available_time() == 13
    assert owner.get_preferences() == ["quiet", "morning walks"]
    owner.update_info("Alex", 8, 18)
    assert owner.name == "Alex"
    assert owner.available_hours_start == 8
    assert owner.available_hours_end == 18


def test_schedule_filters_and_orders_tasks():
    owner, pet = make_owner_and_pet()
    high = Task("Morning walk", 30, "high")
    medium = Task("Feed", 15, "medium")
    low = Task("Brush", 20, "low")
    pet.add_task(high)
    pet.add_task(medium)
    pet.add_task(low)

    schedule = Schedule(pet, None, 60)
    schedule.generate_schedule(pet.list_tasks(), owner)

    assert len(schedule.scheduled_tasks) == 2
    assert schedule.scheduled_tasks[0][0].title == "Morning walk"
    assert schedule.scheduled_tasks[1][0].title == "Feed"
    assert schedule.total_time_used == 45
    assert schedule.is_schedule_valid() is True
