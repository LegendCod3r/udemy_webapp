import time


def get_todos(file_path='todos.txt'):
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, file_path='todos.txt'):
    with open(file_path, 'w') as file_local:
        file_local.writelines(todos_local)


def show_todos(file_path='todos.txt'):
    todos_local = get_todos(file_path)

    new_todos = [item.strip('\n') for item in todos_local]
    for index, item in enumerate(new_todos, start=1):
        row = f"{index} - {item}"
        print(row)


# Create a function to update the clock
def update_clock(window_local, gui_key):
    current_time = time.strftime("%I:%M:%S %p")
    window_local[gui_key].update(current_time)
