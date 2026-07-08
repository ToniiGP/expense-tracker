from storage import save_expenses, load_expenses
from expense import Expense
from datetime import date 

CATEGORIES = [
    "Food",
    "Transportation",
    "Entertainment",
    "Bills",
    "Shopping",
    "Health",
    "Other"
]


def add_expense(expenses): 
    
    expense_id = len(expenses) + 1
    
    amount = get_amount()
    
    category = get_category()
    
    description = get_description()
            
    date = get_date()
    
    expense = Expense(expense_id, amount, category, description, date)
    expenses.append(expense)
    save_expenses(expenses)
    
    print("Expense added successfully!")
    

def get_amount(): 
    
    while True: 
        try: 
            amount = float(input("Enter the expense amount: "))
            if amount <= 0: 
                print("Amount should be a positive value, please try again")
            else:
                return amount
            
        except ValueError: 
            print("Invalid amount. Please enter a valid number.")
            

def get_category(): 
    
    print("Please select one of the following categories: ")
    for category in CATEGORIES: 
        print(f"{category}")
        
    while True: 
        category = input("Enter the expense category: ")
        category = category.title().strip()
        if category in CATEGORIES:
            return category 
        else: 
            print("That's not a valid category please try again!")


def get_description(): 
    
    while True: 
        description = input("Enter the expense description: ")
        description = description.strip()
        
        if description: 
            return description
        
        print("Description cannot be empty. Please try again.")


def get_date(): 
    return date.today().isoformat()
            
    
def view_expenses(expenses): 
    
    if expenses:
        print("\nExpenses: ")
        for expense in expenses: 
            print(expense)
    else: 
        print("There are no expenses in the system.")
        
        

def get_expense_id(): 
    while True: 
        try: 
            expense_id = int(input("Enter the id of the expense you want to delete: "))
            if expense_id <= 0: 
                print("ID should be a positive  whole number, please try again")
            else:
                return expense_id
            
        except ValueError: 
            print("Invalid ID. Please enter a valid whole number.")
    
    

def delete_expense(expenses): 
    
    if not expenses: 
        print("There are not expenses in the system")
        return 
        
    expense_id = get_expense_id()
    
    for expense in expenses: 
        if expense.id == expense_id: 
            expenses.remove(expense)
            print("Expense removed succesfully")
            save_expenses(expenses)
            return
        
    print(f"Expense {expense_id} doesn't exist")
      
        
def display_menu(): 
    
    print("\nExpenses Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Exit")


def main(): 
    
    expenses = load_expenses()
    
    while True: 
        
        display_menu()
        choice = input("Please choose an option: ")
        
        if choice == "1": 
            add_expense(expenses)
        elif choice == "2": 
            view_expenses(expenses)
        elif choice == "3": 
            delete_expense(expenses)
        elif choice == "4": 
            print("Goodbye!!")
            break
        else: 
            print("Invalid option, please try again!") 



if __name__ == "__main__": 
    main()