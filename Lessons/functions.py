FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the tod-do items  list in the text file."""
#It is recommended to use DocStrings in functions
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print(__name__)

if __name__ == "__lectures__":
    print("Hello")
    print(get_todos())
