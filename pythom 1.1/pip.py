conunt = {}

while True:
    log = input("Enter the option: 1 = Login, 2 = Register, 3 = Exit: ")

    match log:
        case "1":
            print("Login")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in conunt and conunt[username] == password:
                print("Login successful!")

                while True:
                    print(f"\nHello {username}")
                    print("\n--- Menu ---")
                    print("1 = Catalog")
                    print("2 = Cart")
                    print("3 = Waiting time")
                    print("4 = Config account")
                    print("5 = Close account")

                    menu_option = input("Enter the option: ")

                    match menu_option:
                        case "1":
                            print("\n--- Catalog Menu ---")
                        case "2":
                            print("")
                        case "3":
                            print("")
                        case "4":
                            while True:
                                print("\n--- Config Menu ---")
                                print("1 = Phone number")
                                print("2 = User settings")
                                print("3 = Credit card")
                                print("4 = Privacy")
                                print("5 = Back")

                                opc = input("Enter the option: ")

                                match opc:
                                    case "1":
                                         while True:
                                            print("\n--- Phone number options ---:")
                                            print("1 = Delete")
                                            print("2 = Update")
                                            print("3 = Add new number")
                                            print("4 = Back")

                                            opcn = input("Enter the option: ")

                                            match opcn:
                                                case "1":
                                                    print("\n--- Delete phone number ---")
                                                    delete = input("Are you shure 1= del, 2= return: ")
                                                    match delete:
                                                        case "1":
                                                            print("Success. Phone number deleted.")
                                                        case "2":
                                                            print("return to menu config...")
                                                            break
                                                case "2":
                                                    print("\n--- Update phone number ---")
                                                    new = input("Enter the new number: ")
                                                    print(f"Success, phone number updated: {new}")
                                                case "3":
                                                    print("\n--- Add new phone number ---")
                                                    new = input("Enter the new phone number: ")
                                                    print(f"Success, new phone number: {new}")
                                                case "4":
                                                    break
                                                case _:
                                                    print("Invalid option.")

                                    case "2":
                                        while True:
                                            print("\n--- User options ---")
                                            print("1 = Change username")
                                            print("2 = Change profile photo")
                                            print("3 = Back")

                                            opcu = input("Enter the option: ")

                                            match opcu:
                                                case "1":
                                                    nom = input("Enter new username: ")
                                                    print(f"Success, new username is {nom}")
                                                case "2":
                                                    print("Photo selected successfully.")
                                                case "3":
                                                    break
                                                case _:
                                                    print("Invalid option.")

                                    case "3":
                                         while True:
                                            print("\n--- Credit Card ---")
                                            print("1 = Credit card info")
                                            print("2 = Add new credit card")
                                            print("3 = Back")
                                        
                                            opcu = input("Enter the option: ")

                                            match opcu:
                                                case "1":
                                                    nom = input("Enter new username: ")
                                                    print(f"Success, new username is {nom}")
                                                case "2":
                                                    print("Photo selected successfully.")
                                                case "3":
                                                    break
                                                case _:
                                                    print("Invalid option.")


                                    case "4":
                                        print("Privacy settings updated.")

                                    case "5":
                                        break

                                    case _:
                                        print("Invalid option.")

                        case "5":
                            print("Account closed. Logging out...")
                            break

                        case _:
                            print("Invalid option.")

            else:
                print("Invalid username or password.")

        case "2":
            print("Register")
            new_user = input("Enter new username: ")

            if new_user in conunt:
                print("That username already exists. Try another one.")
            else:
                new_phonenumber = input("Enter phone number: ")
                new_email = input("Enter the email: ")
                new_pass = input("Enter the password: ")
                conunt[new_user] = new_pass
                print(f"User '{new_user}' registered successfully.")

        case "3":
            print("Goodbye!")
            break

        case _:
            print("Invalid option.")
