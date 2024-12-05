# Imports
from machine import Pin
from time import sleep
from neopixel import NeoPixel
# Setup light strip NOTE: Red5v to PIN 40, BlackGND to PIN 38, GreenData to PIN 34
strip = NeoPixel(Pin(28), 15)  # 15 LEDs on GPIO 28
HIT_COLOUR = (0, 0, 255)
DELTA_SPEED = 0.25

# Clear all LEDs
def clearLEDs():
    for i in range(15):
        strip[i] = (0, 0, 0) # type: ignore
    strip.write()

# Set passed LED to a set colour
def setLED(index):
    strip[index] = HIT_COLOUR # type: ignore
    strip.write()

def bounce_mode(delta_speed, target_i):
    i = 0
    is_ascending = True
    while True:
        try:
            clearLEDs()
            setLED(i)
            sleep(delta_speed)  # sleep before moving
            if is_ascending:
                if i < 14: i+= 1                # If i is less than 15, increment i
                else: is_ascending = False      # Otherwise, set is_ascending to False so teh leds move in the opposite direction
            else:
                if i > 0: i-= 1                 # If i is greater than 0, decrement i
                else: is_ascending = True       # Otherwise, set is_ascending to True so the leds move in the opposite direction
        except KeyboardInterrupt:  # If the user presses Ctrl+C
                score = abs(target_i - i)  # Calculate the score, based on how many LEDs away the target was
                return score
        
get_perc_score = lambda x: round(((15-x)/15*100), 1)  # Calculate the percentage score based on the number of LEDs away the target was to 1 DP

# Main program
t_led = int(input("Enter the target LED (0 to 14 inclusive): "))  # Get the target LED from the user
raw_score = bounce_mode(DELTA_SPEED, t_led)  # Start the game on bounce setting
print("Score: ", get_perc_score(raw_score))  # Print the score
clearLEDs()  # Reset lights when finished

# Reese : Gorgeous RPI code