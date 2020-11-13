class Room:
    def __init__(self, name, max_capacity, room_price):
        self.name = name
        self.max_capacity = max_capacity
        self.room_price = room_price
        self.guests = []
        self.song_queue = []
    
    def guest_count(self):
        return len(self.guests)

# Checks in guests individually and adds them to room guest list
    def check_in_guest(self, guest):
        self.guests.append(guest)

# if given guest is in room guest list, this removes them (checks them out)
    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

# Seeing as people usually come to karaoke in groups, this calls the check_in_guest function for each guest in a group list.
    def check_in_group(self, group):
        for guest in group:
            self.check_in_guest(guest)

# Checks guests out one by one in a group, as above.      
    def check_out_group(self, group):
        for guest in group:
            self.check_out_guest(guest)

# Adds song one at a time to a room's song_queue list    
    def add_song_to_queue(self, new_song):
        self.song_queue.append(new_song)