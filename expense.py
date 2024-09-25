from datetime import datetime

class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.strptime(date, "%Y-%m-%d").date()

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.strftime("%Y-%m-%d")
        }

def filter_expenses(expenses, start_date, end_date, category=None):
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()
    
    filtered = [exp for exp in expenses if start <= exp.date <= end]
    
    if category:
        filtered = [exp for exp in filtered if exp.category == category]
    
    return filtered