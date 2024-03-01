import math
def func_radius():
    while True:
        global radius
        try:
            radius = float(input("What is the radius of this circle in cm: "))
            calculations()
        except ValueError:
            print("Please enter a valid input.")
            
def calculations():
    while True:
        shape = input("Is your shape a circle or a sphere?")
        if shape == "circle":
            circle()
        elif shape == "sphere":
            sphere()
        else:
            print("Please enter a valid input, ensure that the type of shape is correct and that none of the letters are capitalised.")

def circle():
    area = math.pi * pow(radius, 2)
    circumference = 2 * math.pi * radius
    print(f"The radius is {radius}, the area is {area} and the circumference is {circumference}.")
    func_radius()
    
def sphere():
    volume = (4/3) * math.pi * pow(radius, 3)
    sphere_area = 4 * math.pi * pow(radius, 2)
    print(f"The radius is {radius}, the volume of the sphere is {volume} and the curved surface area is {sphere_area}.")
    func_radius()
if __name__ == "__main__":
    func_radius()
