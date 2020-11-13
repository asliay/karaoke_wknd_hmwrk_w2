class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.bill = 0.00

    def remove_cash(self, cash_amount):
        self.wallet -= cash_amount
    
    def add_to_bill(self, bill_amount):
        self.bill += bill_amount

    def buy_drink(self, drink):
        self.wallet -= drink.price
        self.bill += drink.price

    