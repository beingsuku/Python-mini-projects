import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "expenses.json"
expense=[]
    

def add_expense():
    amt=float(input("Enter amount:"))
    cat=input("Enter Category:")
    des=input("Enter Description:")
    expense_data={
    "amount":amt,
    "category":cat,
    "description":des
    }
    expense.append(expense_data)
    save_expenses()


def view_expense():
    if not expense:
        print("You haven't Spent yet!")
        return
    count=1
    for i in expense:
        print(count)
        print("Amount:",i["amount"])
        print("Category:",i["category"])
        print("Description:",i["description"])
        count+=1


def total_spending():
    if not expense:
        print("You haven't Spent yet!")
        return
    total=0
    for i in expense:
      total+=i["amount"]
    print(total)

def category_summary():
    if not expense:
        print("You haven't Spent yet!")
        return
    category_totals = {}
    for i in expense:
        category=i["category"]
        amount=i["amount"]
        if category in category_totals:
            category_totals[category]+=amount
        else:
            category_totals[category]=amount

    print("--Spending by category--")
    for category , amount in category_totals.items():
        print(f"{category}:₹{amount:.2f}")
    
def save_expenses():
    with open(DATA_FILE, "w") as f:
        json.dump(expense,f,indent=4)

def load_expenses():
    global expense
    try:
        with open(DATA_FILE, "r") as f:
            expense=json.load(f)
    except FileNotFoundError:
        print("No saved expenses found.Starting Fresh!!")

def main():
    load_expenses()
    choice=0
    while choice!=5:
        print("1.Add expense 2.View Expenses 3.Total Spending 4.Category Summary 5.Exit\n ")
        choice=int(input("Enter choice:"))
        match choice:
            case 1:
                add_expense()
            case 2:
                view_expense()
            case 3:
                total_spending()
            case 4:
                category_summary()
            case 5:
                print("Thank you for using Expense Tracker!!")
            case _:
                print("Enter a valid option")

main()
