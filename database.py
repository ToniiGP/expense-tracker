import sqlite3

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