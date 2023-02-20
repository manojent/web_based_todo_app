FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """This function reads a .txt file
    and returns the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """This function writes the to-do item list
    to a .txt file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print('Hello from functions')
    print(get_todos())

