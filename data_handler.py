import json
from expense import Expense

def save_expenses(expenses):
    with open('data/expenses.json', 'w') as f:
        json.dump([exp.to_dict() for exp in expenses], f)

def load_expenses():
    try:
        with open('data/expenses.json', 'r') as f:
            data = json.load(f)
            return [Expense(**exp) for exp in data]
    except FileNotFoundError:
        return []