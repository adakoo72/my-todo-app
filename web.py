import streamlit as st
import functions

LOCAL_FILE = "todos.txt"

todos = functions.get_todos(LOCAL_FILE)


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, LOCAL_FILE)


st.title("Adam's Todo App")
st.subheader("Make this a sub-header")
st.write("Use this application to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:  # if checkbox is checked (True)
        todos.pop(index)  # remove from list
        functions.write_todos(todos, LOCAL_FILE)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter new todo:", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")