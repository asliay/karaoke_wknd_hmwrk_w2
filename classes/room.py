class Room:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.guests = []
        self.song_queue = []
    
    def guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        if guest in self.guests:
            self.guests.remove(guest)

    def check_in_group(self, group):
        for guest in group:
            self.check_in_guest(guest)
        
    def check_out_group(self, group):
        for guest in group:
            self.check_out_guest(guest)
    
    def add_song_to_queue(self, new_song):
        self.song_queue.append(new_song)