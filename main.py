from storage import save_expenses, load_expenses
from expense import Expense
from input_helpers import get_amount, get_category, get_date, get_description, get_expense_id
 

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
    

def view_expenses(expenses): 
    
    if expenses:
        print("\nExpenses: ")
        for expense in expenses: 
            print(expense)
    else: 
        print("There are no expenses in the system.")
        
        
def delete_expense(expenses): 
    
    if not expenses: 
        print("There are no expenses in the system.")
        return 
        
    expense_id = get_expense_id()
    
    for expense in expenses: 
        if expense.id == expense_id: 
            expenses.remove(expense)
            print("Expense removed successfully.")
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