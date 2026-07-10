class User:
    def __init__(self, user_id, name, age, gender, phone, email, password):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.password = password

    def display(self):
        print("\n----- User Profile -----")
        print(f"User ID : {self.user_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Gender  : {self.gender}")
        print(f"Phone   : {self.phone}")
        print(f"Email   : {self.email}")

class Train:
    def __init__(self, train_no, train_name, source, destination,
                 departure_time, arrival_time, total_seats,
                 available_seats, fare):
        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.fare = fare

    def display_train(self):
        print("\n----- Train Details -----")
        print(f"Train No : {self.train_no}")
        print(f"Train    : {self.train_name}")
        print(f"Route    : {self.source} -> {self.destination}")
        print(f"Departure: {self.departure_time}")
        print(f"Arrival  : {self.arrival_time}")
        print(f"Seats    : {self.available_seats}/{self.total_seats}")
        print(f"Fare     : ₹{self.fare}")

    def check_availability(self):
        return self.available_seats > 0

    def book_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            return True
        return False

    def cancel_seat(self):
        if self.available_seats < self.total_seats:
            self.available_seats += 1
class Passenger:
    def __init__(self, passenger_id, name, age, gender, berth_preference):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender
        self.berth_preference = berth_preference

    def display(self):
        print("\n----- Passenger Details -----")
        print(f"Passenger ID : {self.passenger_id}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")
        print(f"Gender       : {self.gender}")
        print(f"Berth Pref.  : {self.berth_preference}")
class Ticket:
    def __init__(self, pnr, user_id, passenger, train,
                 journey_date, seat_no, fare, status="Confirmed"):
        self.pnr = pnr
        self.user_id = user_id
        self.passenger = passenger
        self.train = train
        self.journey_date = journey_date
        self.seat_no = seat_no
        self.fare = fare
        self.status = status
    def print_ticket(self):
        print("\n========== TICKET ==========")
        print(f"PNR           : {self.pnr}")
        print(f"Passenger     : {self.passenger.name}")
        print(f"Age/Gender    : {self.passenger.age}/{self.passenger.gender}")
        print(f"Train No      : {self.train.train_no}")
        print(f"Train Name    : {self.train.train_name}")
        print(f"Route         : {self.train.source} -> {self.train.destination}")
        print(f"Journey Date  : {self.journey_date}")
        print(f"Seat No       : {self.seat_no}")
        print(f"Fare          : ₹{self.fare}")
        print(f"Status        : {self.status}")
        print("============================")
        
class ReservationSystem:
    def __init__(self):
        self.users = []
        self.trains = []
        self.bookings = []

    def add_user(self, user):
        self.users.append(user)

    def add_train(self, train):
        self.trains.append(train)

    def add_booking(self, ticket):
        self.bookings.append(ticket)

    def get_users(self):
        return self.users

    def get_trains(self):
        return self.trains

    def get_bookings(self):
        return self.bookings