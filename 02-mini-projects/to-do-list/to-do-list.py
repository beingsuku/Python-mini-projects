tasks=[]
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "tasks.json"
def save_tasks():
       with open("tasks.json", "w") as f:
          json.dump(tasks, f)

def load_tasks():
       global tasks
       try:
           with open(DATA_FILE, "r") as f:
              tasks = json.load(f)
       except FileNotFoundError:
          tasks = []
def add_task():
    task= input("Enter a task ,the realistic one!:")
    tasks.append(task)
    save_tasks()

def view_tasks():
    if not tasks:
        print("You have'nt added a task yet!")
        return 
    for i in range(len(tasks)):
        print(i+1,".",tasks[i])

def remove_task():
    if not tasks:
        print("You have'nt added a task yet!")
        return 
    view_tasks()
    try:
        to_remove=int(input("Enter which task you wanna remove:"))
        removed = tasks.pop(to_remove-1)
        print(f"Removed as you said Majesty: {removed}")
        save_tasks()
    except (ValueError,IndexError):
        print("That's not a valid task,Enter a valid one gurlll!")

def main():
    load_tasks()
    while True:
          print("1.Add task\n2.View\n3.Remove\n4.Exit")
          try:
            choice= int(input("Choose:"))
          except ValueError:
              print("Please enter a number babe!")
              continue
          match choice:
            case 1:
                add_task()
            case 2:
                view_tasks()
            case 3:
                remove_task()
            case 4 :
                print("Successfully executed!")
                break
            case _ :
                print("Invalid input!!")

main()
                
            



