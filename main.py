# To Do app

def to_do_app():
    # Initialize an empty list to store tasks
    total_tasks = []
    print("----- WELCOME TO TASK MANAGER -----\n")
    
    # Prompt user for the number of tasks to perform
    while True:
        try:
            no_of_tasks = int(input('How many tasks you want to perform: '))
            # Check if the input is a positive number
            if no_of_tasks <= 0:
                print('Please enter a positive number.')
                continue
            break
        except ValueError:
            # Handle non-integer input
            print('Enter a valid number, not a string or letters')

    # Loop to add tasks based on user input
    for i in range(1, no_of_tasks + 1):
        name_of_task = input(f'Add task no {i}: ').lower()
        total_tasks.append(name_of_task)  # Append each task to the task list
        
    # Display all tasks added by the user
    print(f'\nToday\'s Tasks are:\n{str(total_tasks)}')
        
    # Main loop for the task management menu
    while True:
        # Display task management options
        print(f'\nSelect One Option:')
        print('1. Add a new task')
        print('2. Update an existing task')
        print('3. View Task List')
        print('4. Delete a task')
        print('5. Exit the application')
        
        try:
            # Prompt user for an option to perform a specific action
            perform_task = int(input('Enter task number you want to perform: '))
        except ValueError:
            # Handle non-integer input for the task selection
            print('Please enter a valid number for task selection.')
            continue

        # Option 1: Add a new task
        if perform_task == 1:
            new_task = input('Which new task you want to add in your today\'s tasks: ').lower()
            # Check if the task already exists
            if new_task in total_tasks:
                print(f'Task "{new_task}" is already present in your tasks.')
            else:
                total_tasks.append(new_task)
                print(f'Task added successfully: {new_task}')
                print(f'Updated Tasks: {total_tasks}')
                
        # Option 2: Update an existing task
        elif perform_task == 2:
            previous_task = input('Enter Task Name which You want to Update: ').lower()
            # Check if the task to update exists
            if previous_task in total_tasks:
                update_task_name = input("Enter New Task: ")
                indx = total_tasks.index(previous_task)
                total_tasks[indx] = update_task_name  # Update the task in the list
                print(f'Updated List is\n {total_tasks}')
                
            else:
                print(f'Task {previous_task} is not present in the List')
                
        # Option 3: View the current task list
        elif perform_task == 3:
            print(f'Your Task List Is Showing Below\n{total_tasks}')

        # Option 4: Delete a specific task
        elif perform_task == 4:
            del_task = input('Enter The Name of Task Which You Want To Delete: ')
            # Check if the task to delete exists
            if del_task in total_tasks:
                total_tasks.remove(del_task)  # Remove the task from the list
                print(f'New List is\n{total_tasks}')    

            else:
                print(f'Task {del_task} is not in the list. Please enter a task that is present.')
        
        # Option 5: Exit the application
        elif perform_task == 5:
            print(f'You closed the app. See you next time!\nTHANK YOU!!!')
            break

# Run the to-do app function
to_do_app()