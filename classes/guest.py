class Guest:
    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash
        self.bill = 0

#Charges an individual guest the total cost of the room
    def guest_pay_for_room(self, room):
        self.cash -= room.room_price