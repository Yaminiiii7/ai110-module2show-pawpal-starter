from pawpal_system import Pet, Task


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
