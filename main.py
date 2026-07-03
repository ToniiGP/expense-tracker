from expense import Expense

CATEGORIES = [
    "Food",
    "Transportation",
    "Entertainment",
    "Bills",
    "Shopping",
    "Health",
    "Other"
]

expenses = []

def add_expense(expenses): 
    expense_id = len(expenses) + 1
    
    amount = float(input("Enter the expense amount: "))
    
    while True: 
        category = input("Enter the expense category: ")
        if category in CATEGORIES:
            break
        else: 
            print("That's not a valid category please try again!")
            
    description = input("Enter the expense description: ")
    date = input("Enter the expense date: ")
    
    expense = Expense(expense_id, amount, category, description, date)
    expenses.append(expense)
    
    print("Expense added successfully!")
    

def view_expenses(expenses): 
    
    if expenses:
        print("\nExpenses: ")
        for expense in expenses: 
            print(expense)
    else: 
        print("There are not expenses in the system.")
        
        
def display_menu(): 
    
    print("\nExpenses Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Exit")


def main(): 
    
    while True: 
        display_menu()
        choice = input("Please choose an option: ")
        
        if choice == "1": 
            add_expense(expenses)
        elif choice == "2": 
            view_expenses(expenses)
        elif choice == "3": 
            print("Goodbye!!")
            break
        else: 
            print("Invalid option, please try again!") 



if __name__ == "__main__": 
    main()