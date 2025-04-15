todo = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo_item = input("Enter a todo item: ")
            todo.append(todo_item)
            print(f"Todo item '{todo_item}' added.")
        case "show":
            if todo:
                print("Todo items:")
                for index, item in enumerate(todo):
                    print(f"{index + 1}. {item}")
            else:
                print("No todo items found.")
        case "edit":
            try:
                index = int(input("Enter the index of the todo item to edit: ")) - 1
                if 0 <= index < len(todo):
                    new_item = input("Enter the new todo item: ")
                    todo[index] = new_item
                    print(f"Todo item at index {index + 1} updated to '{new_item}'.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        case "complete":
            try:
                index = int(input("Enter the index of the todo item to complete: ")) - 1
                if 0 <= index < len(todo):
                    completed_item = todo.pop(index)
                    print(f"Todo item '{completed_item}' completed and removed from the list.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        case "exit":
            break
        case _:
            print("Invalid command. Please try again.")
            