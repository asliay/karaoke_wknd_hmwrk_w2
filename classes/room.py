class Room:
    def __init__(self, name, max_capacity, room_price, song_catalogue):
        self.name = name
        self.max_capacity = max_capacity
        self.room_price = room_price
        self.song_catalogue = song_catalogue
        self.guests = []
        self.song_queue = []
    
    def guest_count(self):
        return len(self.guests)

    def song_count(self):
        return len(self.song_queue)

# Checks in guests individually and adds them to room guest list (if there is space)
    def check_in_guest(self, guest):
        if len(self.guests) < self.max_capacity and guest.age >= 18:
            self.guests.append(guest)
        elif guest.age < 18:
            return "Sorry! You have to be at least 18 to come in."
        elif  len(self.guests) == self.max_capacity:
            return "Sorry! This room is full!"
        
# Returns a warning string if guests > room capacity
    def capacity_reached(self):
        if len(self.guests) >= self.max_capacity:
            return "Sorry! This room is full!"

# Seeing as people usually come to karaoke in groups, this calls the check_in_guest function for each guest in a given group list.
    def check_in_group(self, group_list):
        for guest in group_list:
            self.check_in_guest(guest)

# Settles customer tab, charges customer for their share of room cost and decreases their cash amount
    def charge_for_room_share(self, guest):
        guest.settle_drink_tab()
        guest.wallet -= (self.room_price) / (len(self.guests))

# Charges customer their share of the room cost, settles their tab, and checks them out (removes from room)
    def check_out_guests(self, guests):
        for guest in self.guests:
            self.charge_for_room_share(guest)
        self.guests.clear()

