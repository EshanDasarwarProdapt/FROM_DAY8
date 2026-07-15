def _validate_number(value, name):
    # Reject bool as it is a subclass of int in Python.
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be an int or float")


def add(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a / b


def get_numbers():
    """Read two numbers from the user."""
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None


def main():
    while True:
        print("\n===== Calculator Menu =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting Calculator...")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please try again.")
            continue

        a, b = get_numbers()
        if a is None:
            continue

        try:
            if choice == "1":
                print("Result:", add(a, b))
            elif choice == "2":
                print("Result:", subtract(a, b))
            elif choice == "3":
                print("Result:", multiply(a, b))
            elif choice == "4":
                print("Result:", divide(a, b))
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except TypeError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()