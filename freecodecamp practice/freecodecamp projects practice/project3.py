class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = list()
        self.balance = 0
        self.withdraw_amount=0
        self.deposit_amount=0

    def deposit(self, amount, description=""):
        deposit_dict = {"amount": amount, "description": description}
        self.ledger.append(deposit_dict)
        self.deposit_amount+=amount
        self.balance += amount

    def withdraw(self, withdraw_amount, withdraw_desciption=""):
        if self.check_funds(withdraw_amount):
            self.withdraw_amount += withdraw_amount
            self.balance -= withdraw_amount
            withdraw_dict = {"amount": - withdraw_amount, "description": withdraw_desciption}
            self.ledger.append(withdraw_dict)

        return self.check_funds(withdraw_amount)

    def get_balance(self):
        return self.balance

    def check_funds(self, fund_amount):
        return fund_amount <= self.get_balance()

    def transfer(self, transfer_amount, transfer_category):
        if self.check_funds(transfer_amount):
            self.withdraw(transfer_amount, f"Transfer to {transfer_category.category_name}")
            transfer_category.deposit(transfer_amount, f"Transfer from {self.category_name}")
        return self.check_funds(transfer_amount)

    def __repr__(self):
        returned_string=self.category_name.capitalize().center(30, "*")+"\n"
        for item in self.ledger:
            item_amount = f'{item["amount"]:.2f}'
            returned_string += item['description'].ljust(23," ")[:23]+ str(item_amount).rjust(7," ") +"\n"
        returned_string += "Total: " + str(self.balance)
        return  returned_string





def create_spend_chart(categories):
    categories_name = list()
    categories_withdraw_amount = list()
    total_withdraw =0
    for category in categories:
        categories_name.append(category.category_name)
        categories_withdraw_amount.append(category.withdraw_amount)
        total_withdraw += category.withdraw_amount

    longest_string_length = len(max(categories_name, key=len))
    returned_string = "Percentage spent by category\n"
    for i in range(11):
        label = f'{100-(i*10)}| '
        returned_string += label.rjust(5," ")
        for j in range(len(categories)):
            if (categories_withdraw_amount[j]/ total_withdraw)*10 > 10-i:
                returned_string += "o  "
            else:
                returned_string += "   "
        returned_string+="\n"
    returned_string += "    ----------"
    for i in range(longest_string_length):
        returned_string += "\n     "
        for k in range(len(categories)):
            returned_string += categories_name[k].ljust(longest_string_length, " ")[i].ljust(3, " ")



    return returned_string


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
create_spend_chart([business, food, entertainment])