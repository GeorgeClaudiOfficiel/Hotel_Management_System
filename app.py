from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Dictionaries to act as my database
rooms = {}
guests = {}
bookings = {}
invoices = {}
next_room_id = 1
next_guest_id = 1
next_booking_id = 1
next_invoice_id = 1


# Home page route
@app.route('/')
def index():
    return render_template('index.html', rooms=rooms, guests=guests, bookings=bookings)

# The room route 
@app.route('/add_room', methods=['POST'])
def add_room():
    global next_room_id
    room_type = request.form['room_type']
    price = request.form['price']
    room = {'id': next_room_id, 'type': room_type, 'price': price, 'booked': False}
    rooms[next_room_id] = room
    next_room_id += 1
    return redirect(url_for('index'))


# Registration route for a new booking
@app.route('/register_guest', methods=['POST'])
def register_guest():
    global next_guest_id
    name = request.form['name']
    contact = request.form['contact']
    guest = {'id': next_guest_id, 'name': name, 'contact': contact}
    guests[next_guest_id] = guest
    next_guest_id += 1
    return redirect(url_for('index'))

# Booking route for a new space
@app.route('/create_booking', methods=['POST'])
def create_booking():
    global next_booking_id
    guest_id = int(request.form['guest_id'])
    room_id = int(request.form['room_id'])
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    if room_id in rooms and guest_id in guests:
        room = rooms[room_id]
        if not room['booked']:
            booking = {'id': next_booking_id, 'guest_id': guest_id, 'room_id': room_id, 'start_date': start_date, 'end_date': end_date, 'active': True}
            bookings[next_booking_id] = booking
            room['booked'] = True
            next_booking_id += 1
    return redirect(url_for('index'))


@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    global next_invoice_id
    booking_id = int(request.form['booking_id'])
    if booking_id in bookings:
        booking = bookings[booking_id]
        total_amount = rooms[booking['room_id']]['price']  # Simplified
        invoice = {'id': next_invoice_id, 'booking_id': booking_id, 'total_amount': total_amount}
        invoices[next_invoice_id] = invoice
        next_invoice_id += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
