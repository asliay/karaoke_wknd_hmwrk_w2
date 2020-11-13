class Room:
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.guests = []
        self.song_queue = []
    
    def guest_count(self):
        return len(self.guests)



    def check_in_group(self, new_group):
        self.guests.extend(new_group)

  