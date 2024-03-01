def main():
    while True:
        global height
        global weight
        try:
            height = float(input("What is your height in cm?: "))
            weight = float(input("What is your weight in kilograms?: "))
            calculate_bmi()
        except ValueError:
            print("Please enter a valid integer in cm.")

def calculate_bmi():
    BMI = float(weight / pow(height / 100, 2))
    print(f"Your BMI is {BMI}.")
if __name__ == "__main__":
    main()
