class Expense: 
    def __init__(self, expense_id, amount, category, description, date): 
        self.id = expense_id
        self.amount = amount 
        self.category = category 
        self.description = description
        self.date = date 
    
    def __str__(self): 
        
        description = self.description 
        
        if len(description) > 30: 
            description = description[:27] + "..."
            
        return(
        f"{self.id:<4}"
        f"${self.amount:<10.2f}"
        f"{self.category:<18}"
        f"{description:<30}"
        f"{self.date}"
    )
        
    