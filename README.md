# ExpenseFlow

A Python-based expense tracker with JSON data persistence and spending analysis.

## Features

- Add and view expenses
- Calculate total spending
- Category-wise spending analysis
- Find highest expense
- Search expenses by category
- Delete expenses
- Input validation
- JSON-based data persistence

## Technologies Used

- Python
- JSON
- File Handling
- Exception Handling

## Project Structure

```text
ExpenseFlow/
├── .gitignore
├── expense_tracker.py
└── README.md

expenses.json is created automatically when expenses are added and is excluded from Git tracking to keep personal expense data private.

How It Works

ExpenseFlow allows users to record expenses by entering the date, category, description, and amount.

The application stores expense data locally in a JSON file and provides basic spending analysis, including total spending, category-wise spending, and the highest expense.

 🚀 How to Run

Clone the Repository
git clone https://github.com/ayushi857-dev/ExpenseFlow.git
Navigate to the Project
cd ExpenseFlow
Run the Application
python expense_tracker.py
Example
================================
       EXPENSE TRACKER
================================
Track your spending and manage your money.

----------- MENU -----------
1. Add Expense
2. View All Expenses
3. View Total Spending
4. Category Analysis
5. Highest Expense
6. Search Expense
7. Delete Expense
8. Exit
----------------------------
Data Storage

ExpenseFlow uses expenses.json for local data persistence.

Example:

[
    {
        "date": "11-09-2026",
        "category": "Food",
        "description": "Lunch",
        "amount": 250
    }
]

The JSON file is generated automatically when an expense is added.

Future Improvements
Edit existing expenses
Monthly and yearly spending reports
Budget tracking
Data visualization
SQLite database integration
GUI or web-based interface
Project Status

Version 1.0 — Completed

Author

Ayushi Shukla

⭐ If you find this project useful, consider giving it a star!


