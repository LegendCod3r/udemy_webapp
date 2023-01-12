import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    if st.session_state["new_todo"] != "":
        todo = st.session_state["new_todo"] + "\n"
        todos.append(todo)
        functions.write_todos(todos)
    else:
        pass


# layout
st.title("My Todo App")
st.write("Increase your productivity.")
for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")
