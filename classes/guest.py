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

# Adds song one at a time to a room's song_queue list    
    def add_song_to_queue(self, room, new_song):
        room.song_queue.append(new_song)

# If a guest's favourite song is on the playlist, they will recognise it and celebrate.
    def recognise_favourite_song(self, room):
        for song in room.song_queue:
            if song.name == self.favourite_song:
                return "Yaaay! I love this song!!"

# Pays customer's drink tab
    def settle_drink_tab(self):
        self.remove_cash(self.drink_tab)

    
    