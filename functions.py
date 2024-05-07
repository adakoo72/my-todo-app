FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Opens a file and reads each line, returning a
    list of to-do items
    """
    # Better way to work with files
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes the to-dos to a text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# print(__name__)
# Don't execute if called from outside functions.py (this file)

if __name__ == "__main__":
    print("Hello, how are you")
    print(get_todos())