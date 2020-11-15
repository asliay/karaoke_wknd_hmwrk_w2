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

#Empties room guest list + song queue
    def check_out_guests(self):
        self.guests.clear()
        self.song_queue.clear()

# Adds song one at a time to a room's song_queue list (and stops people queuing the same song multiple times!)   
    def add_song_to_queue(self, new_song):
        if new_song not in self.song_queue:
            self.song_queue.append(new_song)
        else:
            return "Not again! Pick another song!"
            
# Searches for song in a room's catalogue by name.
    def search_song_catalogue_by_name(self, song_name):
        for song in self.song_catalogue:
            if song.name == song_name:
                return song.name

# If a guest's favourite song is coming up on the room's song queue, they will recognise it and celebrate.
    def recognise_favourite_song(self, guest):
        for guest in self.guests:
            for song in self.song_queue:
                if song.name == guest.favourite_song:
                    return "Yaaay! I love this song!!"

