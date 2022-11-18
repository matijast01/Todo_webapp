FILEPATH = "todo_list.txt"


def get_todo_list(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    try:
        with open(filepath, "r") as file_local:
            todo_list_local = file_local.readlines()
    except FileNotFoundError:
        todo_list_local = []

    return todo_list_local


def write_todo_list(todo_list_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todo_list())
