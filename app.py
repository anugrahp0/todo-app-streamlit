import streamlit as st
import functions

todos = functions.view_tasks()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.add_task(todos)

st.header("My Todo App")
st.subheader("This is my to-do app.")

# Add unique keys to each checkbox
for index, todo in enumerate(todos):
    if todo:
        checkbox = st.checkbox(todo, key=f"{index}")
        if checkbox:
            todos.pop(index)
            functions.add_task(todos)
            del st.session_state[index]
            st.rerun()
st.text_input(label="Todo", placeholder="Add new todo", on_change=add_todo, key="new_todo")


st.session_state
