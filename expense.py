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
        f"{self.date:<25}"
    )
        
    def to_dict(self): 
        return{
            "id:" : self.id,
            "amount" : self.amount, 
            "category:" : self.category,
            "description:" : self.description, 
            "date:" : self.date
        }
    
    @classmethod
    def from_dict(cls, expense_data):
        return cls(
            expense_data["id:"],
            expense_data["amount"],
            expense_data["category:"],
            expense_data["description:"],
            expense_data["date:"]
    )   