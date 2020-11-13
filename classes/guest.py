class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.bill = 0.00

    def buy_drink(self, drink):
        self.wallet -= drink.price
        self.bill += drink.price

    