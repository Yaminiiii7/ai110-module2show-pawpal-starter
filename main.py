from pawpal_system import Owner, Pet, Scheduler, Task


if __name__ == "__main__":
    owner = Owner("Jordan", 7, 20)

    mochi = Pet("Mochi", "dog", age=3, breed="Golden Retriever")
    luna = Pet("Luna", "cat", age=2, breed="Siamese")

    owner.add_pet(mochi)
    owner.add_pet(luna)

    mochi.add_task(Task("Morning walk", 30, "high", "exercise"))
    mochi.add_task(Task("Feed breakfast", 10, "high", "feeding"))
    mochi.add_task(Task("Playtime", 20, "medium", "enrichment"))
    mochi.add_task(Task("Grooming", 25, "low", "care"))

    luna.add_task(Task("Feed dinner", 10, "high", "feeding"))
    luna.add_task(Task("Litter cleanup", 15, "medium", "care"))

    scheduler = Scheduler(mochi, None, 90)
    planned_tasks = scheduler.build_plan_for_owner(owner, available_minutes=90)

    print(f"Today's Schedule for {owner.name}")
    print(scheduler.display_plan())
    print()
    print("Reasoning:")
    print(scheduler.get_reasoning())
    print()
    print(f"Planned tasks: {len(planned_tasks)}")
