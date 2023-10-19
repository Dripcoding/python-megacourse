import streamlit as st
import functions
import uuid

# obtain todos from file
todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    if todo not in todos:
        todos.append(todo + '\n')
        functions.write_todos(todos)
        st.session_state['new_todo'] = ''


st.title('My Todo App')
st.subheader('This is my todo app.')
st.write('This app is meant to increase your productivity.')

for todo in todos:
    st.checkbox(todo)

# adding a new todo
st.text_input(label=' ', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')


st.session_state
