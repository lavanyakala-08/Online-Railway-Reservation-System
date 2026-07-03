from database import initialize_database
import user
import booking

def main_menu():
    initialize_database()
    current_user_id = None

    while True:
        print("\n=== ONLINE RAILWAY RESERVATION SYSTEM ===")
        if not current_user_id:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                email = input("Email: ")
                res = user.register_user(username, password, email)
                print(res["message"])
            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                res = user.login_user(username, password)
                print(res["message"])
                if res["status"] == "success":
                    current_user_id = res["user_id"]
            elif choice == "3":
                break
        else:
            print("\n1. View Available Trains")
            print("2. Book a Ticket")
            print("3. View My Bookings")
            print("4. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                trains = booking.view_trains()
                for t in trains:
                    print(f"ID: {t['train_id']} | {t['train_name']} | {t['source']} -> {t['destination']} | Seats Left: {t['available_seats']}")
            elif choice == "2":
                train_id = int(input("Enter Train ID: "))
                seats = int(input("Number of seats to book: "))
                res = booking.book_ticket(current_user_id, train_id, seats)
                print(res["message"])
            elif choice == "3":
                history = booking.get_user_bookings(current_user_id)
                if not history:
                    print("No bookings found.")
                for b in history:
                    print(f"Booking ID: {b['booking_id']} | {b['train_name']} ({b['source']} to {b['destination']}) | Seats: {b['seats_booked']} | Date: {b['booking_date']}")
            elif choice == "4":
                current_user_id = None
                print("Logged out successfully.")

if __name__ == "__main__":
    main_menu()
