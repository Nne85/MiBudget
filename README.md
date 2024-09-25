# Personal Budget Tracker App

This is a simple Python-based personal budgeting app that allows users to set an overall monthly budget, define spending limits for categories (such as food, entertainment, bills, etc.), and track expenses. The app provides a user-friendly interface to input budgets and expenses, view total spending by category, and save the data to a JSON file for persistence.

## Features

- **Set Overall Monthly Budget**: Define an overall monthly budget for all categories.
- **Define Category Budgets**: Set specific spending limits for categories such as food, transportation, entertainment, etc.
- **Add Expenses**: Input individual expenses under specific categories.
- **Track Spending**: View total spending by category and compare it against the budget.
- **Save Data**: All expenses are saved to a JSON file for persistence.
- **Date Filtering**: Filter expenses by month to get detailed monthly spending reports.

## Project Structure

```bash
budget_tracker_app/
│
├── main.py                   # Entry point for the application
├── budget.py                 # Contains the logic for managing budgets and expenses
├── ui.py                      # Contains the UI logic (using tkinter)
├── expense.py                 # Contains the expense logic
├── data/                      # Directory for storing data (like JSON files)
│   └── expenses.json          # File to persist expense data
└── README.md                  # Project documentation

## Getting Started
Prerequisites
To run the app, you'll need:

Python 3.x installed on your machine.
The tkinter library, which is usually included with Python installations.

## Installation
Clone this repository to your local machine:
git clone https://github.com/Nne85/MiBudget.git

Navigate to the project directory:
cd MiBudget

Ensure the required directories and files are present:

data/expenses.json will be created automatically when you save data for the first time.
Running the Application
To start the application, run the following command in the terminal or command prompt:
python main.py

##  Usage
Set Monthly Budget: Enter your total monthly budget in the appropriate field and click "Set Monthly Budget."

Add Category Budgets: Enter a category (e.g., Food, Bills) and a budget for that category. Then click "Add Category Budget."

Add Expenses: Enter the category, the amount, a brief description, and the date (YYYY-MM-DD) of the expense. Then click "Add Expense" to track it.

View Spending: Click the "View Spending" button to see a summary of your total spending for the current month, categorized by each budget.

Save Expenses: After adding expenses, click "Save Expenses" to persist the data in a JSON file (data/expenses.json).

Contact
If you have any questions or suggestions, feel free to reach out!

Email: nneukamaka@gmail.com