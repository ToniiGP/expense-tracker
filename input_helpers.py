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

def get_expense_id(): 
    while True: 
        try: 
            expense_id = int(input("Enter the id of the expense:  "))
            if expense_id <= 0: 
                print("ID should be a positive  whole number, please try again")
            else:
                return expense_id
            
        except ValueError: 
            print("Invalid ID. Please enter a valid whole number.")