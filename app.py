import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.
This version connects the Streamlit UI to the Python logic layer so your pet data persists while you use the app.
"""
)

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan", 7, 20)

owner = st.session_state.owner

st.subheader("Owner Profile")
owner_name = st.text_input("Owner name", value=owner.name)
if st.button("Save owner"):
    owner.update_info(owner_name, owner.available_hours_start, owner.available_hours_end)
    st.session_state.owner = owner
    st.success("Owner updated.")

st.divider()

st.subheader("Add a Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
age = st.number_input("Age", min_value=0, max_value=30, value=2, step=1)

if st.button("Add pet"):
    pet = Pet(pet_name, species, age=age)
    owner.add_pet(pet)
    st.session_state.owner = owner
    st.success(f"{pet_name} added to your household.")

if owner.pets:
    st.subheader("Your Pets")
    for pet in owner.pets:
        pet_age = pet.age if pet.age is not None else "unknown"
        st.write(f"- {pet.name} ({pet.species}, age {pet_age})")
else:
    st.info("No pets yet. Add one above to get started.")

st.divider()

st.subheader("Add a Task")
if owner.pets:
    selected_pet_name = st.selectbox("Pet", [pet.name for pet in owner.pets])
    pet = next(pet for pet in owner.pets if pet.name == selected_pet_name)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        task = Task(task_title, int(duration), priority)
        pet.add_task(task)
        st.session_state.owner = owner
        st.success(f"{task_title} added to {pet.name}.")
else:
    st.info("Add a pet first so you can create tasks.")

st.divider()

st.subheader("Build Schedule")
if st.button("Generate schedule"):
    if owner.pets:
        scheduler = Scheduler(owner.pets[0], None, 90)
        all_tasks = []
        for pet in owner.pets:
            all_tasks.extend(pet.list_tasks())
        scheduler.generate_schedule(all_tasks, owner)
        st.write(scheduler.display_plan())
        st.caption(scheduler.get_reasoning())
    else:
        st.info("Add a pet and some tasks to generate a schedule.")
