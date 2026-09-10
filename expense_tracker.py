## Expense Tracker ##
import json

# File where expenses will be permanently stored
FILE_NAME = "expenses.json"

# List to store all expenses
expenses = []


# Load expenses from JSON file
def load_expenses():
    global expenses

    try:
        with open(FILE_NAME, "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        # If file does not exist, start with an empty list
        expenses = []

    except json.JSONDecodeError:
        # If JSON file is empty or damaged
        expenses = []


# Save expenses to JSON file
def save_expenses():
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense():
    print("\n--- Add New Expense ---")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    # Validate amount
    while True:
        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    # Add expense to list
    expenses.append(expense)

    # Save updated list to JSON file
    save_expenses()

    print("\nExpense added successfully!")


# View all expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses added yet.")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(f"\nExpense {i}")
        print(f"Date: {expense['date']}")
        print(f"Category: {expense['category']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: ₹{expense['amount']:.2f}")


# Calculate total spending
def total_spending():
    if not expenses:
        print("\nNo expenses added yet.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Spending: ₹{total:.2f}")


# Show category-wise spending
def category_analysis():
    if not expenses:
        print("\nNo expenses added yet.")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category] = 0

        categories[category] += expense["amount"]

    print("\n--- Category-wise Spending ---")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# Find the highest expense
def highest_expense():
    if not expenses:
        print("\nNo expenses added yet.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n--- Highest Expense ---")
    print(f"Date: {highest['date']}")
    print(f"Category: {highest['category']}")
    print(f"Description: {highest['description']}")
    print(f"Amount: ₹{highest['amount']:.2f}")


# Search expenses by category
def search_expenses():
    if not expenses:
        print("\nNo expenses added yet.")
        return

    search_category = input("\nEnter category to search: ").lower()

    found = False

    print("\n--- Search Results ---")

    for expense in expenses:
        if expense["category"].lower() == search_category:
            print(f"\nDate: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Amount: ₹{expense['amount']:.2f}")

            found = True

    if not found:
        print("No expenses found for this category.")


# Delete an expense
def delete_expense():
    if not expenses:
        print("\nNo expenses added yet.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        removed_expense = expenses.pop(number - 1)

        # Save updated data
        save_expenses()

        print("\nExpense deleted successfully!")
        print(f"Deleted: {removed_expense['description']} - ₹{removed_expense['amount']:.2f}")

    except ValueError:
        print("Please enter a valid number.")


# Main program
load_expenses()

print("\n================================")
print("       EXPENSE TRACKER")
print("================================")
print("Track your spending and manage your money.")


while True:

    print("\n----------- MENU -----------")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Category Analysis")
    print("5. Highest Expense")
    print("6. Search Expense")
    print("7. Delete Expense")
    print("8. Exit")
    print("----------------------------")

    try:
        choice = int(input("\nEnter your choice: "))

    except ValueError:
        print("Please enter a number between 1 and 8.")
        continue


    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        total_spending()

    elif choice == 4:
        category_analysis()

    elif choice == 5:
        highest_expense()

    elif choice == 6:
        search_expenses()

    elif choice == 7:
        delete_expense()

    elif choice == 8:
        print("\nThank you for using Expense Tracker!")
        print("Your expenses have been saved.")
        break

    else:
        print("Invalid choice. Please try again.")
