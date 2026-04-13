from tracker import expenses

def category_summary():
    summary ={}
    for expense in expenses:
        amount = expense[1]
        category = expense[2]
        summary[category] = summary.get(category , 0)+ amount

        if not summary:
            print("NO data found")
            return
        
        print("Category summary ")
        for category, total in summary.items():
            print(f"{category} : ${total}")

def highest_spending_category():
    summary ={}
    for expense in expenses:
        amount= expense[1]
        category = expense[2]
        summary[category] = summary.get(category , 0)+ amount

        if not summary:
            print("NO data found")
            return
        
        highest= max(summary ,key=summary.get)
        print(f"Highest spent is{highest} (${summary[highest]})")


