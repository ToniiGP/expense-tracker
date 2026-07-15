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
        print("-" * 75)
        print(f"{'ID':<4}{'Amount':<11}{'Category':<18}{'Description':<30}{'Date'}")
        print("-" * 75)
        
        for expense in expenses: 
            print(expense)
        print("-" * 75)
        
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


def view_statistics(expenses): 
    if not expenses: 
        print("There are no expenses in the system")
        return 
    
    total = 0 
    max_amount = 0 
    min_amount = expenses[0].amount
    
    for expense in expenses: 
        total += expense.amount
        if expense.amount > max_amount: 
            max_amount = expense.amount 
        if expense.amount < min_amount: 
            min_amount = expense.amount 
                
    avg = total / len(expenses)
    print("========== Expense Statistics ==========")
    print(f"Total amount spent: ${total:.2f}")
    print(f"Average: ${avg:.2f}")
    print(f"Highest expense: ${max_amount:.2f}")
    print(f"Lowest expense: ${min_amount:.2f}")
    print("========================================")
    
def filter_expenses_category(expenses): 
    
    if not expenses:
        print("There are not expenses in the system") 
        return
        
    category = get_category()
    matching_expenses = []
    for expense in expenses: 
        if expense.category == category: 
            matching_expenses.append(expense)
        
    if not matching_expenses: 
        print("No expenses exist with that category")
    else: 
        view_expenses(matching_expenses)
        
        
def filter_expenses_description(expenses):
    
    if not expenses: 
        print("There are not expenses in the system") 
        return
    
    matching_expenses = []
    word = input("Enter a keyword to search for (example: coffee):").strip()
    
    for expense in expenses: 
        if word.lower() in expense.description.lower(): 
            matching_expenses.append(expense)
            
    if not matching_expenses: 
        print("No expenses match your search.")
    else: 
        view_expenses(matching_expenses)
    

def generate_expense_id(expenses): 
    if not expenses: 
        return 1 
    
    max_id = 0 
    
    for expense in expenses: 
        if expense.id > max_id:
            max_id = expense.id 
    
    return max_id + 1 