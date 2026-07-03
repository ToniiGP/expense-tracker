class Expense: 
    def __init__(self, expense_id, amount, category, description, date): 
        self.id = expense_id
        self.amount = amount 
        self.category = category 
        self.description = description
        self.date = date 
    
    def __str__(self): 
        return f"ID: {self.id} | AMOUNT: ${self.amount:.2f} | CATEGORY: {self.category} | DESC: {self.description} | DATE: {self.date}"
        
        
        
        