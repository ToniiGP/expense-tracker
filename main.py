from storage import load_expenses
from expense_manager import add_expense, view_expenses, delete_expense, edit_expense
 
def display_menu(): 
    
    print("\nExpenses Tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Edit expense")
    print("5. Exit")


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
            edit_expense(expenses)
        elif choice == "5": 
            print("Goodbye!!")
            break
        else: 
            print("Invalid option, please try again!") 



if __name__ == "__main__": 
    main()