from Todo import TodoApplication
from Error.error import *
import os


def main() -> None:
    app = TodoApplication("0193d14")
    app.setup()

    while True:
        print("---------------< Todo >---------------")
        app.view()
        print("--------------------------------------")
        command = input(">>>").strip().lower()

        command = command.split()
        if len(command) >= 2 and command[0] == 'todo':
            command.pop(0)
        else:
            os.system("cls")
            print("\nError: Unknown command.")
            continue
        
        # clear command line
        os.system("cls") 
        
        operator = command.pop(0)

        # Create new todo list
        if operator == "-cl":
            if len(command)!= 0:
                list_name = ' '.join(command)
                try:
                    app.create_new_list(list_name)
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -cl <list-name>")

        # Delete a todo list
        elif operator == "-del":
            if len(command) == 1:
                list_ID = command.pop(0)
                try:
                    app.delete_list(list_ID)
                except TodolistNotFoundError:
                    print("\nError: list-ID is wrong")
                except CantChangeDefaultListsError:
                    print("\nError: You can't remove the default todo lists")
                except:
                    print("\nError: Unknown error occurred")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -del <list-ID>")
    
        # Rename a todo list                
        elif operator == "-rn":
            if len(command) >= 2:
                list_ID = command.pop(0)
                new_name = ' '.join(command)
                try:
                    app.rename_list(list_ID, new_name)
                except TodolistNotFoundError:
                    print("\nError: list-ID is wrong")
                except CantChangeDefaultListsError:
                    print("\nError: You can't change the name of the default lists")
                except:
                    print("\nError: Unknown error occurred")
                else:
                    print("\ndone!")            
            else:
                print("\nError: command syntaxt is wrong, try: todo -rn <list-ID> <new-name>")

        # Exit from app
        elif operator == "-exit":
            print("Exit...")
            exit()
        
        # Open a todo list
        elif len(command) == 0:
            try:
                res = app.get_list(operator)
            except TodolistNotFoundError:
                print("\nError: task-ID is wrong.")
            except:
                print("\nError: Unknown error occurred")
            else:
                list_section(res)
        
        else:
            print("\nError: Unknown command.")

def list_section(todo):
    while True:
        print("===================// {};".format(todo.name))
        todo.view()
        command = input("\n>>>").strip().lower()

        command = command.split()
        if len(command) >= 2 and command[0] == "todo":
            command.pop(0)
        else:
            os.system("cls")
            print("\nError: Unknown command.")
            continue
        
        # clear command line
        os.system("cls") 

        operator = command.pop(0)

        # Create a task
        if operator == "-ct":
            if len(command) != 0:
                task_title = ''
                task_description = ''

                if '-d' not in command:
                    task_title = ' '.join(command)
                    task_description = None
                
                else:
                    while len(command) > 0:
                        element = command.pop(0)
                        if element == "-d":
                            task_description = None if len(command) == 0 else ' '.join(command)
                            break
                        else:
                            task_title += element
                try:
                    todo.add_task(task_title, task_description)
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo <title> -d <description>")

        # Delete a task
        elif operator == "-del":
            if len(command) == 1:
                task_ID = command.pop(0)
                try:
                    todo.delete_task(task_ID)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong")
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -del <task-ID>")
        
        # mark a task as done   
        elif operator == "-done":
            if len(command) == 1:
                task_ID = command.pop(0)
                try:
                    todo.mark_as_done(task_ID)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong")
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -done <task-ID>")
        
        # mark a task as undone
        elif operator == "-undone":
            if len(command) == 1:
                task_ID = command.pop(0)
                try:
                    todo.mark_as_undone(task_ID)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong")
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("Error: command syntaxt is wrong, try: todo -undone <task-ID>")

        # add to myday
        elif operator == "-add-myday":
            if len(command) == 1:
                task_ID = command.pop(0)
                try:
                    todo.add_to_myday(task_ID)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong")
                except NotImplementedError:
                    print("\nError: This function isn't work in this list")
                except AlreadySetError:
                    print("\nError: Your task already added to 'myday'")
                except:
                    print("\nError: Unknown error occurred")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -add-myday <task-ID>")
        
        # remove from myday
        elif operator == "-rem-myday":
            if len(command) == 1:
                task_ID = command.pop(0)
                try:
                    todo.remove_from_myday(task_ID)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong.")
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -add-myday <task-ID>")

        # add to important list        
        elif operator == "-add-imp":
            if len(command) == 1:
                task_ID = command.pop(0)
                try:
                    todo.mark_as_important(task_ID)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong")
                except NotImplementedError:
                    print("\nError: This function isn't work in this list")
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -add-imp <task-ID>")

        # remove from important list
        elif operator == "-rem-imp":
            "mark_as_important"
            if len(command) == 1:
                task_ID = command.pop(0)
                try:
                    todo.mark_as_notimportant(task_ID)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong")
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    print("\ndone!")
            else:
                print("\nError: command syntaxt is wrong, try: todo -rem-imp <task-ID>")

        # back to home
        elif operator == "-home":
            return

        else:
            if len(command) == 0:
                try:
                    task = todo.get_task(operator)
                except TaskNotFoundError:
                    print("\nError: task-ID is wrong.")
                except:
                    print("\nError: Unknown error occurred.")
                else:
                    task_section(task)
            else:
                print("Error: Unknown command.")
            
def task_section(task):
    while True:
        print("="*45)
        print("{}".format(task.title))
        print("="*45)
        print("State: {}\nDate: {}".format("done" if task.state else "undone", '-/-/-' if task.date is None else task.date))
        print("description: {}".format("No description" if task.description is None else task.description))

        command = input("\n>>> ").strip().lower()

        command = command.split()
        if len(command) >= 2 and command[0] == "todo":
            command.pop(0)
        else:
            os.system("cls")
            print("\nError: Unknown command.")
            continue
        
        # clear command line
        os.system("cls")

        operator = command.pop(0)
        if operator == "-edit-title":
            if len(command) != 0:
                new_title = ' '.join(command)
                task.title = new_title
            else:
                print("\nError: command syntaxt is wrong, try: todo -edit-title <new-title>")
        
        elif operator == "-edit-date":
            if len(command) == 1:
                new_date = command.pop(0)
                task.date = new_date
            else:
                print("\nError: command syntaxt is wrong, try: todo -edit-date <date>")
        
        elif operator == "-edit-desc":
            if len(command) != 0:
                new_description = " ".join(command)
                task.description = new_description
            else:
                print("\nError: command syntaxt is wrong, try: todo -edit-desc <description>")
        
        elif operator == "-back":
            return

        else:
            print("\nError: Unknown command.")

if __name__ == "__main__":
    main()
