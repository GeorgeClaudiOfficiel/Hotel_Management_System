class Room:
    def __init__(self, room_number, room_type, price):
        """
         This method initializes the attributes shown above for the 'Room' instance
         """
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True
        
    def update_room(self, room_number = None, room_type = None):
        """
        """