from expense import Expense
from storage import save_expenses
from input_helpers import get_amount, get_category, get_date, get_description, get_expense_id

def add_expense(expenses): 
    
    expense_id = generate_expense_id(expenses)
    
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
    
    
def edit_expense(expenses): 
    if not expenses:
        print("There are no expenses in the system.")
        return
    
    view_expenses(expenses)
    
    expense_id = get_expense_id()
    
    for expense in expenses: 
        if expense.id == expense_id: 
            
            print("Please choose one of the following options for the field you would like to modify: ")
            print("1. Amount")
            print("2. Category")
            print("3. Description")
            selection = input("enter option number: ")
                
            if selection == "1": 
                expense.amount = get_amount()
            elif selection == "2": 
                expense.category = get_category()
            elif selection == "3": 
                expense.description = get_description()
            else: 
                print("That's not a valid option please try again")
                    
            
            save_expenses(expenses)
            print("Expense updated successfully.")
            return
            
    print(f"Expense {expense_id} doesn't exist.")
                    
    
    

def generate_expense_id(expenses): 
    if not expenses: 
        return 1 
    
    max_id = 0 
    
    for expense in expenses: 
        if expense.id > max_id:
            max_id = expense.id 
    
    return max_id + 1 