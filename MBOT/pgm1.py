import random
import time

# Define functions for the actions
def speak(message):
    print(f"Bot says: {message}")

def drive_forward():
    print("Driving forward")

def drive_back():
    print("Driving back")
    time.sleep(2)

def turn_randomly():
    direction = random.choice(["left", "right"])
    print(f"Turning {direction}")
    time.sleep(2)

def open_trash_can():
    print("Opening trash can lid")

def close_trash_can():
    print("Closing trash can lid")

def detect_obstacle(distance):
    return distance < 20

def detect_garbage_type():
    # Use voice recognition to detect garbage type
    return random.choice(["plastic", "paper", "glass"])

# Main loop
while True:
    drive_forward()

    # Simulate ranging sensor detecting an obstacle
    obstacle_detected = detect_obstacle(random.randint(0, 50))

    if obstacle_detected:
        drive_back()
        turn_randomly()
    else:
        open_trash_can()

        # Wait for human to throw trash
        time.sleep(5)

        close_trash_can()

        # Detect if trash has been thrown out
        trash_thrown_out = detect_obstacle(random.randint(0, 50))

        if trash_thrown_out:
            speak("Thank you for throwing out the trash.")
            garbage_type = detect_garbage_type()
            speak(f"Please throw the {garbage_type} into the corresponding trash can.")
            # Open the corresponding trash can lid
            # ...

        # Continue driving forward
