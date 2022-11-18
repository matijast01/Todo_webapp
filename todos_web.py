import streamlit as st
import functions

todo_list = functions.get_todo_list()


def add_todo():
    if st.session_state["new_todo"] != "":
        todo_local = st.session_state["new_todo"] + "\n"
        todo_list.append(todo_local)
        functions.write_todo_list(todo_list)


st.title("Todo App")
st.subheader("Keep track of what you need to do.")
st.write("List of todos:")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo_list(todo_list)
        del st.session_state[index]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todo...",
              key="new_todo", on_change=add_todo)
