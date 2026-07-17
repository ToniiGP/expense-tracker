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
    
    cursor = connection.execute(
        
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
    
    expense_id = cursor.lastrowid
    connection.close()
    
    return expense_id

    
def load_expenses_from_db(): 
    
    expenses = []
    
    connection = sqlite3.connect(DATABASE_FILE)
    
    cursor = connection.execute(
        """
        SELECT id, amount, category, description, date
        FROM expenses
        ORDER BY id
        """
    )
    rows = cursor.fetchall()
    
    for row in rows:
        expenses.append(Expense(*row))
    
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
    

def update_expense_in_db(expense):
    
    connection = sqlite3.connect(DATABASE_FILE)
    
    connection.execute(
        """
        UPDATE expenses
        SET amount = ?,
            category = ?,
            description = ?,
            date = ?
        WHERE id = ?
        """,
        (
            expense.amount,
            expense.category,
            expense.description,
            expense.date,
            expense.id
        )
    )
    
    connection.commit()
    connection.close()
    

    
    
    
    
    