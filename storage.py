import csv 

def export_to_csv(expenses): 
    
    if not expenses: 
        print("There are not expenses to export")
        return 
    
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        
        writer.writerow(["ID", "Amount", "Category", "Description", "Date"])
        
        for expense in expenses: 
            writer.writerow([
                expense.id,
                expense.amount,
                expense.category,
                expense.description,
                expense.date
            ])
            
    print("Expenses successfully exported to expenses.csv.")
        
    