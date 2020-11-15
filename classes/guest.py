class Guest:
    def __init__(self, name, age, favourite_song, wallet):
        self.name = name
        self.age = age
        self.favourite_song = favourite_song
        self.wallet = wallet
        self.drink_tab = 0.00

# Decrease cash in guest's wallet
    def remove_cash(self, cash_amount):
        self.wallet -= cash_amount

# Add amount to drink tab    
    def add_to_tab(self, bill_amount):
        self.drink_tab += bill_amount

# Customer orders drink - adds drink_price to drink_tab
    def order_drink(self, drink):
            self.add_to_tab(drink.price)

# Pays customer's drink tab
    def settle_drink_tab(self):
        self.remove_cash(self.drink_tab)


            





    
    