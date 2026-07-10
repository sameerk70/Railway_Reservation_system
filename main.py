from services import RailwayService

service = RailwayService()

while True:
    print("\n========== Railway Reservation System ==========")
    print("1. Register")
    print("2. User Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        service.register_user()

    elif choice == "2":
        user = service.login_user()

        if user:
            while True:
                print("\n========== User Menu ==========")
                print("1. Search Train")
                print("2. Book Ticket")
                print("3. Cancel Ticket")
                print("4. My Bookings")
                print("5. Change Password")
                print("6. Logout")

                user_choice = input("Enter your choice: ")
                if user_choice == "1":
                    service.search_train()

                elif user_choice == "2":
                    service.book_ticket(user)

                elif user_choice == "3":
                    service.cancel_ticket(user)

                elif user_choice == "4":
                    service.view_bookings(user)

                elif user_choice == "5":
                    service.change_password(user)

                elif user_choice == "6":
                    print("Logged Out Successfully!")
                    break

                else:
                    print("Invalid Choice!")
    elif choice == "3":
         if service.admin_login():
            while True:
                print("\n========== Admin Menu ==========")
                print("1. Add Train")
                print("2. View All Trains")
                print("3. Update Train")
                print("4. Delete Train")
                print("5. View All Bookings")
                print("6. Logout")

                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    service.add_train()

                elif admin_choice == "2":
                    service.view_all_trains()

                elif admin_choice == "3":
                    service.update_train()

                elif admin_choice == "4":
                    service.delete_train()

                elif admin_choice == "5":
                    service.view_all_bookings()

                elif admin_choice == "6":
                    print("Admin Logged Out Successfully!")
                    break

                else:
                    print("Invalid Choice!")

    elif choice == "4":
        print("Thank You for Using Railway Reservation System!")
        break

    else:
        print("Invalid Choice!")