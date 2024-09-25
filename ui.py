import tkinter as tk
from tkinter import ttk, messagebox
from budget import Budget
from expense import Expense
from data_handler import save_expenses, load_expenses

class BudgetApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal Budget App")
        self.master.geometry("600x400")

        self.budget = Budget()
        self.expenses = load_expenses()

        self.create_widgets()

    def create_widgets(self):
        notebook = ttk.Notebook(self.master)
        notebook.pack(expand=True, fill="both")

        self.budget_frame = ttk.Frame(notebook)
        self.expense_frame = ttk.Frame(notebook)
        self.report_frame = ttk.Frame(notebook)

        notebook.add(self.budget_frame, text="Set Budget")
        notebook.add(self.expense_frame, text="Add Expense")
        notebook.add(self.report_frame, text="View Report")

        self.create_budget_widgets()
        self.create_expense_widgets()
        self.create_report_widgets()

    def create_budget_widgets(self):
        ttk.Label(self.budget_frame, text="Overall Monthly Budget:").grid(row=0, column=0, padx=5, pady=5)
        self.overall_budget_entry = ttk.Entry(self.budget_frame)
        self.overall_budget_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self.budget_frame, text="Set Overall Budget", command=self.set_overall_budget).grid(row=1, column=0, columnspan=2, pady=10)

        ttk.Label(self.budget_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5)
        self.category_entry = ttk.Entry(self.budget_frame)
        self.category_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.budget_frame, text="Category Budget:").grid(row=3, column=0, padx=5, pady=5)
        self.category_budget_entry = ttk.Entry(self.budget_frame)
        self.category_budget_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.budget_frame, text="Set Category Budget", command=self.set_category_budget).grid(row=4, column=0, columnspan=2, pady=10)

    def create_expense_widgets(self):
        ttk.Label(self.expense_frame, text="Amount:").grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(self.expense_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.expense_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.expense_category_entry = ttk.Entry(self.expense_frame)
        self.expense_category_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.expense_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5)
        self.description_entry = ttk.Entry(self.expense_frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(self.expense_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.expense_frame)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(self.expense_frame, text="Add Expense", command=self.add_expense).grid(row=4, column=0, columnspan=2, pady=10)

    def create_report_widgets(self):
        self.report_text = tk.Text(self.report_frame, height=20, width=50)
        self.report_text.pack(padx=10, pady=10)

        ttk.Button(self.report_frame, text="Generate Report", command=self.generate_report).pack(pady=10)

    def set_overall_budget(self):
        try:
            amount = float(self.overall_budget_entry.get())
            self.budget.set_overall_budget(amount)
            messagebox.showinfo("Success", f"Overall budget set to {amount}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the budget")

    def set_category_budget(self):
        try:
            category = self.category_entry.get()
            amount = float(self.category_budget_entry.get())
            self.budget.set_category_budget(category, amount)
            messagebox.showinfo("Success", f"Budget for {category} set to {amount}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the budget")

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.expense_category_entry.get()
            description = self.description_entry.get()
            date = self.date_entry.get()

            expense = Expense(amount, category, description, date)
            self.expenses.append(expense)
            save_expenses(self.expenses)

            messagebox.showinfo("Success", "Expense added successfully")
            self.clear_expense_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter valid values for all fields")

    def clear_expense_entries(self):
        self.amount_entry.delete(0, tk.END)
        self.expense_category_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def generate_report(self):
        self.report_text.delete(1.0, tk.END)
        overall_budget = self.budget.get_overall_budget()
        category_budgets = self.budget.get_all_category_budgets()

        total_spent = sum(expense.amount for expense in self.expenses)
        self.report_text.insert(tk.END, f"Overall Budget: {overall_budget}\n")
        self.report_text.insert(tk.END, f"Total Spent: {total_spent}\n")
        self.report_text.insert(tk.END, f"Remaining: {overall_budget - total_spent}\n\n")

        for category, budget in category_budgets.items():
            category_expenses = [exp for exp in self.expenses if exp.category == category]
            category_total = sum(exp.amount for exp in category_expenses)
            self.report_text.insert(tk.END, f"{category} Budget: {budget}\n")
            self.report_text.insert(tk.END, f"{category} Spent: {category_total}\n")
            self.report_text.insert(tk.END, f"{category} Remaining: {budget - category_total}\n\n")