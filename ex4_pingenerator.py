import random
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
PIN = []
def main():
    global number
    while True:
        try:
            number = int(input("How long do you want this PIN to be?: "))
            generate_pin(number)
        except ValueError:
            print("Please enter a valid number.")
def generate_pin(num_digits):
    for i in range(number):
        pin_number = random.randint(0, 9)
        print(pin_number)
        PIN.append(pin_number)
    print(''.join(map(str, PIN)))
        
           
if __name__ == "__main__":
    main()
