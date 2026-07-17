import sqlite3
from expense import Expense

DATABASE_FILE = "expenses.db"


def initialize_database(): 
    
    connection = sqlite3.connect(DATABASE_FILE)
    
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            amount REAL NOT NULL, 
            category TEXT NOT NULL, 
            description TEXT NOT NULL, 
            date TEXT NOT NULL
        )
        """  
    )
    
    connection.commit()
    connection.close()
    
    
def insert_expense(expense): 
    connection = sqlite3.connect(DATABASE_FILE)
    
    connection.execute(
        
        """
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?,?,?,?)
        """, 
        (
            expense.amount, 
            expense.category, 
            expense.description, 
            expense.date
        )
    )
    
    connection.commit()
    connection.close()
    
    
def load_expenses_from_db(): 
    
    expenses = []
    
    connection = sqlite3.connect(DATABASE_FILE)
    
    cursor = connection.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    
    for row in rows:
        expense = Expense(*row)
        expenses.append(expense)
    
    connection.close()
    
    return expenses 


def delete_expense_from_db(expense_id): 
    
    connection = sqlite3.connect(DATABASE_FILE)
    
    connection.execute(
        
        "DELETE FROM expenses WHERE id = ?", 
        (expense_id,) 
    )    
    
    connection.commit()
    connection.close()
    
    
    
    
    