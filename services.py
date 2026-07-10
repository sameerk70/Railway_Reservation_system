from models import User, Train, Passenger, Ticket, ReservationSystem
from utils import *

USER_FILE = "data/users.json"
TRAIN_FILE = "data/trains.json"
BOOKING_FILE = "data/bookings.json"


class RailwayService:
    def __init__(self):
        self.system = ReservationSystem()
        self.users = load_data(USER_FILE)
        self.trains = load_data(TRAIN_FILE)
        self.bookings = load_data(BOOKING_FILE)

    def register_user(self):
        print("\n========== User Registration ==========")

        name = input("Enter Name: ").strip()

        age = input("Enter Age: ").strip()
        if not validate_age(age):
            print("Invalid age!")
            return

        gender = input("Enter Gender (Male/Female): ").strip()

        phone = input("Enter Phone Number: ").strip()
        if not validate_phone(phone):
            print("Invalid phone number!")
            return

        email = input("Enter Email: ").strip()
        if not validate_email(email):
            print("Invalid email!")
            return

        if find_user_by_email(self.users, email):
            print("Email already exists!")
            return

        password = input("Enter Password: ").strip()
        if not validate_password(password):
            print("Weak password!")
            return

        user = {
            "user_id": len(self.users) + 1,
            "name": name,
            "age": int(age),
            "gender": gender,
            "phone": phone,
            "email": email,
            "password": password
        }

        self.users.append(user)
        save_data(USER_FILE, self.users)

        print("Registration Successful!")
        return user

    def login_user(self):
        print("\n========== User Login ==========")

        email = input("Enter Email: ").strip()
        password = input("Enter Password: ").strip()

        for user in self.users:
            if user["email"] == email and user["password"] == password:
                print(f"\nWelcome, {user['name']}!")
                return user

        print("Invalid Email or Password!")
        return None

    def search_train(self):
        print("\n========== Search Train ==========")

        source = input("Enter Source: ").strip().lower()
        destination = input("Enter Destination: ").strip().lower()

        found = False

        for train in self.trains:
            if (train["source"].lower() == source and
                train["destination"].lower() == destination):

                print("\n------------------------------")
                print(f"Train No   : {train['train_no']}")
                print(f"Train Name : {train['train_name']}")
                print(f"Departure  : {train['departure_time']}")
                print(f"Arrival    : {train['arrival_time']}")
                print(f"Available  : {train['available_seats']}")
                print(f"Fare       : ₹{train['fare']}")
                print("------------------------------")
                found = True

        if not found:
            print("No Train Found!")
        return None

    def book_ticket(self, user):
        print("\n========== Book Ticket ==========")

        train_no = input("Enter Train Number: ").strip()

        train = find_train_by_number(self.trains, train_no)
        if not train:
            print("Train not found!")
            return

        if train["available_seats"] <= 0:
            print("No seats available!")
            return

        name = input("Passenger Name: ").strip()

        age = input("Passenger Age: ").strip()
        if not validate_age(age):
            print("Invalid age!")
            return

        gender = input("Passenger Gender: ").strip()

        journey_date = input("Journey Date (YYYY-MM-DD): ").strip()
        if not validate_date(journey_date):
            print("Invalid date!")
            return

        seat_no = f"S{train['total_seats'] - train['available_seats'] + 1}"
        pnr = generate_pnr()

        booking = {
            "pnr": pnr,
            "user_id": user["user_id"],
            "train_no": train["train_no"],
            "passenger_name": name,
            "age": int(age),
            "gender": gender,
            "journey_date": journey_date,
            "seat_no": seat_no,
            "fare": train["fare"],
            "status": "Confirmed"
        }

        self.bookings.append(booking)
        train["available_seats"] -= 1

        save_data(BOOKING_FILE, self.bookings)
        save_data(TRAIN_FILE, self.trains)

        print("\nTicket Booked Successfully!")
        print("PNR:", pnr)
        print("Seat:", seat_no)
        return None

    def cancel_ticket(self, user):
        print("\n========== Cancel Ticket ==========")

        pnr = input("Enter PNR Number: ").strip()

        for booking in self.bookings:
            if booking["pnr"] == pnr and booking["user_id"] == user["user_id"]:

                if booking["status"] == "Cancelled":
                    print("Ticket already cancelled!")
                    return

                booking["status"] = "Cancelled"

                train = find_train_by_number(self.trains, booking["train_no"])
                if train:
                    train["available_seats"] += 1

                save_data(BOOKING_FILE, self.bookings)
                save_data(TRAIN_FILE, self.trains)

                print("Ticket Cancelled Successfully!")
                return

        print("PNR not found!") 
        return None

    def view_bookings(self, user):
        print("\n========== My Bookings ==========")

        found = False

        for booking in self.bookings:
            if booking["user_id"] == user["user_id"]:

                print("\n----------------------------")
                print(f"PNR          : {booking['pnr']}")
                print(f"Train No     : {booking['train_no']}")
                print(f"Passenger    : {booking['passenger_name']}")
                print(f"Journey Date : {booking['journey_date']}")
                print(f"Seat No      : {booking['seat_no']}")
                print(f"Fare         : ₹{booking['fare']}")
                print(f"Status       : {booking['status']}")
                print("----------------------------")

                found = True

        if not found:
            print("No bookings found!")
        return None

    def change_password(self, user):
        print("\n========== Change Password ==========")

        old_password = input("Enter Old Password: ").strip()

        if old_password != user["password"]:
            print("Incorrect old password!")
            return

        new_password = input("Enter New Password: ").strip()

        if not validate_password(new_password):
            print("Weak password!")
            return

        user["password"] = new_password

        for u in self.users:
            if u["user_id"] == user["user_id"]:
                u["password"] = new_password
                break

        save_data(USER_FILE, self.users)
        print("Password changed successfully!")
        return None

    def admin_login(self):
        print("\n========== Admin Login ==========")

        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        if username == "admin" and password == "admin123":
            print("Admin Login Successful!")
            return True
        
        print("Invalid Admin Credentials!")
        return False
    def add_train(self):
        print("\n========== Add Train ==========")

        train = {
            "train_no": input("Train Number: "),
            "train_name": input("Train Name: "),
            "source": input("Source: "),
            "destination": input("Destination: "),
            "departure_time": input("Departure Time: "),
            "arrival_time": input("Arrival Time: "),
            "total_seats": int(input("Total Seats: ")),
            "available_seats": int(input("Available Seats: ")),
            "fare": float(input("Fare: "))
        }

        self.trains.append(train)
        save_data(TRAIN_FILE, self.trains)

        print("Train Added Successfully!")

    def view_all_trains(self):
        print("\n========== All Trains ==========")

        if not self.trains:
            print("No trains available!")
            return

        for train in self.trains:
            print("\n---------------------------")
            print(f"Train No : {train['train_no']}")
            print(f"Name     : {train['train_name']}")
            print(f"Route    : {train['source']} -> {train['destination']}")
            print(f"Seats    : {train['available_seats']}/{train['total_seats']}")
            print(f"Fare     : ₹{train['fare']}")
    
    def delete_train(self):
        print("\n========== Delete Train ==========")

        train_no = input("Enter Train Number: ").strip()

        for train in self.trains:
            if str(train["train_no"]) == train_no:
                self.trains.remove(train)
                save_data(TRAIN_FILE, self.trains)
                print("Train Deleted Successfully!")
                return

        print("Train Not Found!")

    def update_train(self):
        print("\n========== Update Train ==========")

        train_no = input("Enter Train Number: ").strip()

        train = find_train_by_number(self.trains, train_no)

        if not train:
            print("Train Not Found!")
            return

        train["train_name"] = input("New Train Name: ")
        train["source"] = input("New Source: ")
        train["destination"] = input("New Destination: ")
        train["departure_time"] = input("New Departure Time: ")
        train["arrival_time"] = input("New Arrival Time: ")
        train["fare"] = float(input("New Fare: "))

        save_data(TRAIN_FILE, self.trains)

        print("Train Updated Successfully!")

    def view_all_bookings(self):
        print("\n========== All Bookings ==========")

        if not self.bookings:
            print("No Bookings Found!")
            return

        for booking in self.bookings:
            print("\n----------------------------")
            print(f"PNR        : {booking['pnr']}")
            print(f"User ID    : {booking['user_id']}")
            print(f"Train No   : {booking['train_no']}")
            print(f"Passenger  : {booking['passenger_name']}")
            print(f"Seat       : {booking['seat_no']}")
            print(f"Date       : {booking['journey_date']}")
            print(f"Status     : {booking['status']}")