from tracker import add_expense , show_expenses
from analytics import category_summary , highest_spending_category

def menu():
    while True:
        print("\n=== EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Category Summary")
        print("4. HIghest Spending Category ")
        print("5. Exit")

        choice =input("Enter your choice")
        
        if choice =="1":
            add_expense()
        elif choice== "2":
            show_expenses()
        elif choice== "3":
            category_summary()
        elif choice== "4":
            highest_spending_category()
        elif choice =="5":
            print("Exiting BYE")
            break
        else:
            print("Invalid choice")


menu()    