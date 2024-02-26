print("\n************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses the weather form a list
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call the weather() once the VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forcast of",weatherAlert,
            "weather conditions.")
        print("VRS has been engaged only allowing you to drive 50pmh.")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forcast of",weatherAlert,
            "weather conditions.")
        print("VRS has been engaged only allowing you to drive 40pmh.")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forcast of",weatherAlert,
            "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60pmh.")

vehicleResponseSystem()


