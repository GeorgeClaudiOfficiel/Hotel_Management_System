class Booking:
    def __init__(self, room, guest, booking_id, booking_date, booking_status, check_in_time, check_out_time):
        self.booking_id = booking_id
        self.booking_date = booking_date
        self.booking_status = booking_status
        self.room = room
        self.guest = guest
        self.check_in_time = check_in_time
        self.check_out_time = check_out_time
        
        