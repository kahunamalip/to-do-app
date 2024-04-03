#from functions import get_todos, write_todos
import functions


while True:
    user_action = input("Type, add, show, edit, Done nigga or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

#        write_todos(filepath=FILEPATH, todos_arg=todos)
#for the above line, he wouldn't recommend this method he insists that the arg should come before the filepath to maintain order.
# continuation_ he even claimed since filepath is default(or should I say defined in the function already), there's no need for the argument.
    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            shit = f"{index + 1}.{item}"
            print(shit)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid please.")
            continue

    elif user_action.startswith('Done nigga'):
    # Here we are done with a certain todo and we telling the bitch that we done!!
       try:
            number = int(user_action[10:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove}  was marked as finished chief!"
            print(message)
       except IndexError:
           print("There's no such number on this list you asshole: ")
           continue
    elif 'exit' in user_action:
        break
    else:
        print("What are you even saying sire? ")

print("bye bye bye bye oooooo")
