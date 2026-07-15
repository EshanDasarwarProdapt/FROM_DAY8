class UserAuth:
    def __init__(self):
        # Dictionary to store username and password
        self.users = {
            "admin": "admin@123"
        }

    def register(self, username, password):
        if username in self.users:
            return False

        self.users[username] = password
        return True

    def login(self, username, password):
        return self.users.get(username) == password

    def display_users(self):
        return list(self.users.keys())


def main():
    auth = UserAuth()

    while True:
        print("\n===== User Authentication Menu =====")
        print("1. Register")
        print("2. Login")
        print("3. Display Users")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            if auth.register(username, password):
                print("Registration successful!")
            else:
                print("Username already exists!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            if auth.login(username, password):
                print("Login successful!")
            else:
                print("Invalid username or password!")

        elif choice == "3":
            print("\nRegistered Users:")
            for user in auth.display_users():
                print(user)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()