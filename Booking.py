from database import get_db_connection

def view_trains():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trains")
    trains = cursor.fetchall()
    conn.close()
    return [dict(train) for train in trains]

def book_ticket(user_id, train_id, seats_to_book):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Check seat availability
    cursor.execute("SELECT available_seats FROM trains WHERE train_id = ?", (train_id,))
    train = cursor.fetchone()
    
    if not train:
        conn.close()
        return {"status": "error", "message": "Train not found."}
    
    if train["available_seats"] < seats_to_book:
        conn.close()
        return {"status": "error", "message": "Not enough seats available."}
    
    # Deduct seats and create booking record
    new_seats = train["available_seats"] - seats_to_book
    cursor.execute("UPDATE trains SET available_seats = ? WHERE train_id = ?", (new_seats, train_id))
    
    cursor.execute(
        "INSERT INTO bookings (user_id, train_id, seats_booked) VALUES (?, ?, ?)",
        (user_id, train_id, seats_to_book)
    )
    
    conn.commit()
    conn.close()
    return {"status": "success", "message": f"Successfully booked {seats_to_book} seat(s)!"}

def get_user_bookings(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.booking_id, t.train_name, t.source, t.destination, b.seats_booked, b.booking_date 
        FROM bookings b
        JOIN trains t ON b.train_id = t.train_id
        WHERE b.user_id = ?
    """, (user_id,))
    bookings = cursor.fetchall()
    conn.close()
    return [dict(booking) for booking in bookings]
