
# declarations has to be done in one line
prompt = "Type add, show, or exit: "
# Creates empty List
tasks = []

while True:

    # this indentation is important

    # getting user input
    user_action = input(prompt)
    # this removes trailing zeros
    user_action = user_action.strip()

# is the user types add that means they want to add
#  else they want to show the list of tasks
    match user_action:
        case "add":
            task = input("Enter a todo: ")
            # Adds on to list
            tasks.append(task)
        case "show":
            for item in tasks:
                print(item)
        case "exit":
            break
print("Bye")

#  this is called a list
# todos = [task, task2, task3]
#  this will output the type an argument
# print(type(task))
