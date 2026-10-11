def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Value must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


principal = get_positive_float("Enter the principal amount: ")
rate = get_positive_float("Enter the annual interest rate (%): ")
time_years = get_positive_float("Enter the time in years: ")

final_amount = principal * ((1 + (rate / 100)) ** time_years)
print(f"The final amount is: ${final_amount:.2f}")
