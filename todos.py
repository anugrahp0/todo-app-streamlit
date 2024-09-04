import functions

def main():
    tasks = ["FOO", "BAR"]

    while True:
        print("\nTo-Do App Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Exit")

        choice = input("Choose an option: ")

        match choice:
            case '1':
                tasks = functions.add_task(tasks)
            case '2':
                tasks = functions.view_tasks()
            case '3':
                tasks = functions.remove_task(tasks)
            case '4':
                tasks = functions.edit_task(tasks)
            case '5':
                print("Exiting the app. Goodbye!")
                break
            case _:
                print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
