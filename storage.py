import json
from expense import Expense

EXPENSES_FILE = "expenses.json"

def save_expenses(expenses): 
    
    dict_expenses = [expense.to_dict() for expense in expenses]
    
    with open(EXPENSES_FILE, "w") as file: 
        json.dump(dict_expenses, file, indent=4)


def load_expenses(): 
    
    new_expenses = []
    
    try:
        with open (EXPENSES_FILE, "r") as file: 
            expenses_data = json.load(file)
    except FileNotFoundError: 
        return new_expenses 
        
    for expense_data in expenses_data: 
        expense = Expense.from_dict(expense_data)
        new_expenses.append(expense)
    
    return new_expenses