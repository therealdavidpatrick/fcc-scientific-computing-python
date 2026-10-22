class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        total = 0
        for transaction in self.ledger:
            total += transaction["amount"]
        return total

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def check_funds(self, amount): 
        if amount > self.get_balance(): 
            return False
        else: 
            return True 

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def __str__(self): 
        transactions = []
        for transaction in self.ledger:
            transactions.append(
                transaction["description"][:23].ljust(23)
                + f'{transaction["amount"]:>7.2f}'
            )
        transactions.append(
            "Total: "
            + f'{self.get_balance():.2f}' 
        )
        return self.category.center(30, "*") + "\n" + "\n".join(transactions)

def create_spend_chart(categories):
    spending = {}

    for category in categories:

        spent = 0

        for transaction in category.ledger:
            if transaction["amount"] < 0:
                spent += abs(transaction["amount"])

        spending[category.category] = spent

    name_lengths = []

    for category in categories:
        name_lengths.append(len(category.category))
    
    max_length = max(name_lengths)
    
    label_rows = []

    for i in range(max_length):
        letters = []

        for category in categories:
            if i < len(category.category):
                letters.append(category.category[i])
            else:
                letters.append(" ")

        label_rows.append(letters)

    total_spending = 0

    for value in spending.values():
        total_spending += value

    percentages = {}

    for category_name, category_spending in spending.items(): 
        if total_spending == 0: 
            percentage = 0
        else:
            percentage = (category_spending / total_spending) * 100
            percentage = int(percentage / 10) * 10

        percentages[category_name] = percentage

    chart = []

    for i in range(100, -1, -10):
        row = []

        for category_name, percentage in percentages.items():
            if i <= percentage:
                row.append("o  ")
            else:
                row.append("   ")

        completed_row = "".join(row)
        chart.append(f"{i:>3}| {completed_row}")
        
    chart.append("    " + "-" * (len(categories) * 3 + 1))

    for row in label_rows:
        chart.append("     " + "  ".join(row) + "  ")

    return "Percentage spent by category" + "\n" + "\n".join(chart)

food = Category("FOOD")
gas = Category("GAS")
clothing = Category("CLOTHING")

categories = [food, gas, clothing]

food.deposit(50)
gas.deposit(30)
clothing.deposit(20)

food.withdraw(50)
gas.withdraw(30)
clothing.withdraw(20)

print(create_spend_chart(categories))
