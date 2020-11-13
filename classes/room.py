class Room:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.guests = []
        self.song_queue = []
    
    def guest_count(self):
        return len(self.guests)

    def add_guests(self, new_guest):
        self.guests.append(new_guest)