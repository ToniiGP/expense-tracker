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
    
    amount = get_amount()
    
    category = get_category()
            
    description = input("Enter the expense description: ")
    date = input("Enter the expense date: ")
    
    expense = Expense(expense_id, amount, category, description, date)
    expenses.append(expense)
    
    print("Expense added successfully!")
    

def get_amount(): 
    
    while True: 
        try: 
            amount = float(input("Enter the expense amount: "))
            if amount <= 0: 
                print("Amount should be a positive value, please try again")
                continue 
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
            
    
def view_expenses(expenses): 
    
    if expenses:
        print("\nExpenses: ")
        for expense in expenses: 
            print(expense)
    else: 
        print("There are no expenses in the system.")
        
        
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