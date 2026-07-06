from pawpal_system import Owner, Pet, Scheduler, Task


if __name__ == "__main__":
    owner = Owner("Jordan", 7, 20)

    mochi = Pet("Mochi", "dog", age=3, breed="Golden Retriever")
    luna = Pet("Luna", "cat", age=2, breed="Siamese")

    owner.add_pet(mochi)
    owner.add_pet(luna)

    walk = Task("Morning walk", 30, "high", "exercise", time_of_day="09:00")
    walk.pet_name = mochi.name
    feed = Task("Feed breakfast", 10, "high", "feeding", time_of_day="08:00")
    feed.pet_name = mochi.name
    play = Task("Playtime", 20, "medium", "enrichment", time_of_day="10:00")
    play.pet_name = mochi.name
    grooming = Task("Grooming", 25, "low", "care", time_of_day="11:00")
    grooming.pet_name = mochi.name

    dinner = Task("Feed dinner", 10, "high", "feeding", time_of_day="08:00")
    dinner.pet_name = luna.name
    litter = Task("Litter cleanup", 15, "medium", "care", time_of_day="08:00")
    litter.pet_name = luna.name

    mochi.add_task(walk)
    mochi.add_task(feed)
    mochi.add_task(play)
    mochi.add_task(grooming)
    luna.add_task(dinner)
    luna.add_task(litter)

    scheduler = Scheduler(mochi, None, 90)
    planned_tasks = scheduler.build_plan_for_owner(owner, available_minutes=90)

    print(f"Today's Schedule for {owner.name}")
    print(scheduler.display_plan())
    print()
    print("Sorted by time:")
    for task in scheduler.sort_by_time([walk, feed, play, grooming, dinner, litter]):
        print(f"- {task.time_of_day} {task.title}")
    print()
    print("Filtered incomplete tasks:")
    for task in scheduler.filter_tasks([walk, feed, play, grooming, dinner, litter], completed=False):
        print(f"- {task.title}")
    print()
    print("Conflict warnings:")
    for warning in scheduler.detect_conflicts([feed, dinner, litter]):
        print(f"- {warning}")
    print()

    recurring_task = Task("Water plants", 5, "medium", frequency="daily", time_of_day="07:00")
    recurring_task.pet_name = mochi.name
    next_occurrence = recurring_task.mark_complete()
    print("Recurring task demo:")
    print(f"- Original complete: {recurring_task.is_complete}")
    if next_occurrence:
        print(f"- Next occurrence created: {next_occurrence.title} at {next_occurrence.time_of_day}")

    print()
    print("Reasoning:")
    print(scheduler.get_reasoning())
    print()
    print(f"Planned tasks: {len(planned_tasks)}")
