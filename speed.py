import sys

def calculate_speed(distance, time):
    return distance / time

if __name__ == "__main__":
    # If command-line arguments are provided
    if len(sys.argv) == 3:
        distance = float(sys.argv[1])
        time = float(sys.argv[2])
    else:
        # User input
        distance = float(input("Enter distance (in km): "))
        time = float(input("Enter time (in hours): "))

    speed = calculate_speed(distance, time)
    print(f"Speed = {speed} km/h")