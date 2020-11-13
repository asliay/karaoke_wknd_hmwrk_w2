class Guest:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drink_tab = 0.00

    def remove_cash(self, cash_amount):
        self.wallet -= cash_amount
    
    def add_to_tab(self, bill_amount):
        self.drink_tab += bill_amount

    def order_drink(self, drink):
        self.add_to_tab(drink.price)

    def settle_drink_tab(self):
        self.remove_cash(self.drink_tab)
    