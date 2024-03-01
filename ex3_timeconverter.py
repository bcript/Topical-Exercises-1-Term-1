def main():
    global time
    while True:
        try:
            time = float(input("What is the time you'd like to convert in seconds?: "))
            time_convert()
        except ValueError:
            print("Please enter a valid number.")
def time_convert():
    if time >= 3600:
        seconds = time % 60
        minutes = (time - 3600) // 60
        hours = time // 3600
    else:
        seconds = time % 60
        minutes = time // 60
        hours = time // 3600
    print(f"{time}s is {seconds} seconds, {minutes} minutes and {hours} hours.")
            
if __name__ == "__main__":
    main()
