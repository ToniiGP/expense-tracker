from storage import load_expenses, export_to_csv
from expense_manager import add_expense, view_expenses, delete_expense, edit_expense, view_statistics, filter_expenses_category, filter_expenses_description
 
def display_menu(): 
    print("============================")
    print("Expenses Tracker")
    print("============================")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Edit expense")
    print("5. View statistics")
    print("6. Filter by category")
    print("7. Search description")
    print("8. Export expenses to csv")
    print("9. Exit")


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
            view_statistics(expenses)
        elif choice == "6":
            filter_expenses_category(expenses)
        elif choice == "7":
            filter_expenses_description(expenses)
        elif choice == "8": 
            export_to_csv(expenses)
        elif choice == "9": 
            print("Goodbye!!")
            break
        else: 
            print("Invalid option, please try again!") 

if __name__ == "__main__": 
    main()