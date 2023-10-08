from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherwise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   First step is to add current datetime value to update lastActivity. 
                    Later we check conditions for each value and only if it matches the type 
                    of data we allow to append to the main task. Else it prints error messages.
    """
    task = TASK_TEMPLATE.copy()     # don't delete this; use this task reference for the below requirements
    task['lastActivity'] = datetime.now()       # update lastActivity with the current datetime value
    
    if len(name) != 0:
        if len(description) != 0:
            if len(due) != 0:
                task['name'] = name          # set the name, description, and due date (all must be provided)
                task['description'] = description
                try:
                    task['due'] = str_to_datetime(due) # due date must match formats mentioned in str_to_datetime()  
                    tasks.append(task)                 # add the new task to the tasks list
                    print("New Task added")            # output a message confirming the new task was added
                except ValueError as e:
                    print(f"Date Format Invalid: {e}")
            else:
                print("Date missing")  
        else:
            print("Description missing")     
    else:
        print("Name missing")      
    save()                                  # make sure save() is still called last in this function

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   Fetch name, description and due of the index task given. We show the old data 
                    in TODOtask and input the new updated data which is further passed to update_task.
    """    
    index = index
    if index >=0 and index < len(tasks):    # consider index out of bounds scenarios 
        task = tasks[index]                 # get the task by index 
        name = input(f"What's the name of this task? TODO task: {task['name']} \n").strip()
        desc = input(f"What's a brief descriptions of this task? TODO description: {task['description']} \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) TODO due: {task['due']} \n").strip()
        update_task(index,name=name, description=desc, due=due)
    else:
        print("Invalid Index Value")        # include appropriate message(s) for invalid index

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   Check if name, description or due have been updated for the index task given. Update it in the original task.
    """ 
    index = index 
    if index >=0 and index < len(tasks): # consider index out of bounds scenarios
        task = tasks[index]              # find the task by index
        
        if len(name) != 0:
            task['name'] = name              # update incoming task data if it's provided
            if len(description) != 0:
                task['description'] = description
                if len(due) != 0:
                    # try:
                    task['due'] = str_to_datetime(due)
                    # except ValueError as e:
                    #     print(f"Date Format Invalid: {e}")
        if (len(name)==0 and len(description)==0 and len(due)==0):
            print("No data to update") 
        else:
            print("Task was updated")     # output that the task was updated if any items were changed
            task['lastActivity'] = datetime.now() # update lastActivity with the current datetime value
    else:
        print("Invalid Index Value")                   # include appropriate message(s) for invalid index

    save()               # make sure save() is still called last in this function

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   Check if task_done in the template is False. If yes then update it with current datetime. Later if we try 
                    to mark the same task it shows that it has already been completed. 
    """ 
    index = index 
    if index >=0 and index < len(tasks):            # consider index out of bounds scenarios   
        task = tasks[index]                         # find task from list by index
        if not task['done']:
            task['done'] = datetime.now()           # if it's not currently marked as done, record the current datetime as the value
        else:
            print("It's already been completed")    # if it is currently done, print a message saying it's already been completed
    else:
        print("Invalid Index Value")                # include appropriate message(s) for invalid index

    save()                                      # make sure save() is still called last in this function

def view_task(index):
    """ View more info about a specific task fetch by index """
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   If condition checks whether the index value is in range from 0 to max length of list, 
                    it further prints the task name, desc and due date. Else, prints an invalid statement
    """
    index = index 
    if index >=0 and index < len(tasks):            # consider index out of bounds scenarios
        task = tasks[index]                         # find task from list by index
                                                    # utilize the given print statement when a task is found
        print(f"""
            [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
            Description: {task['description']} \n 
            Last Activity: {task['lastActivity']} \n
            Due: {task['due']}\n
            Completed: {task['done'] if task['done'] else '-'} \n
            """.replace('  ', ' '))
    else:
        print("Invalid Index Value")                # include appropriate message(s) for invalid index 


def delete_task(index):
    """ deletes a task from the tasks list by index """
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   If condition checks whether the index value is in range from 0 to max length of list, 
                    it further deletes the task or else prints an invalid statement
    """
    index = index 
    if index >=0 and index < len(tasks):
        tasks.pop(index)                         # delete/remove task from list by index
        print("Task deleted successfully")       # message should show if it was successful or not
    else:
        print("Invalid index. Task not found.")  # consider index out of bounds scenarios and include message
    
    save()                                 # make sure save() is still called last in this function

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   The below code checks if any task within tasks has task_done as "False". Prints all incomplete task. 
    """
    _tasks = [task for task in tasks if not task['done']]   # generate a list of tasks where the task is not done 
    list_tasks(_tasks)                                      # pass that list into list_tasks()

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    """ 
        UCID: krs
        Date: 09/26/2023
        Solution:   The below code checks if any task within tasks has task_done as "False" and due date earlier than current date.
                    Later print all overdue tasks. 
    """
    current_datetime = datetime.now()  
    # generate a list of tasks where the due date is older than "now" and that are not complete (i.e., not done)
    _tasks = [task for task in tasks if not task['done'] and str_to_datetime(task['due']) < current_datetime]
    list_tasks(_tasks)                  # pass that list into list_tasks()


def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    """ 
        UCID: krs
        Date: 10/08/2023
        Solution:   The below code checks the due date of task if remaining and then calculate time using current time and duedate time.
                    If any task is already done then it just shows task already completed or else prints the due time. 
                    Time difference is calculated by subtracting due time from current time or vice versa if the task is due.                 
    """
    current_datetime = datetime.now() 
    if index >=0 and index < len(tasks):            # get the task by index
        task = tasks[index]

        if task['done']:
            print("Task Completed already")
        else:
            due_datetime = str_to_datetime(task['due'])
            if due_datetime > current_datetime:         # get the days, hours, minutes, seconds between the due date and now
                time_difference = due_datetime - current_datetime
                days = time_difference.days
                seconds = time_difference.seconds
                hours, seconds = divmod(seconds, 3600)
                minutes, seconds = divmod(seconds, 60)               
                # display the remaining time via print in a clear format showing X days, X hours, X minutes, X seconds
                # example: 1 day, 0 hours, 0 minutes, 0 seconds remaining
                remaining_time = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds remaining"
                print(remaining_time)
            else:
                time_difference = current_datetime - due_datetime
                days = time_difference.days
                seconds = time_difference.seconds
                hours, seconds = divmod(seconds, 3600)
                minutes, seconds = divmod(seconds, 60)
                # if the due date is in the past print out how many days, hours, minutes, seconds the task is overdue
                # example: 0 days, 2 hours, 5 minutes, 10 seconds overdue (note there's no negative values)
                overdue_time = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds overdue"
                print(overdue_time)
            
    else:
        print("Invalid Index Value")  # consider index out of bounds scenarios and include appropriate message(s) for invalid index

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()