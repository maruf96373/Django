def divide_numbers():
    try:
        # Take two numbers as input
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Perform division
        result = numerator / denominator

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    else:
        print(f"Result: {result}")
    finally:
        print("Thank you for using the division program.")

# Example Usage
if __name__ == "__main__":
    divide_numbers()
