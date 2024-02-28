
#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcomeo Branch Starts here
timeToSleep = 1
print("\n\nWelcome to InforTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsi add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Infotech Center System Booting"+"."* ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r"+ message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating system Booted Up - Retina Scanned - Access Granted!")
#Gasoline Branch Starts Here
print("********************************************************************************")
print("Gasoline Branch\n\n")

#Import Libraries HEre


#Function that list Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function thats lists Gas Stations,m randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Circle K","Mobile","Costco","Meijers","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then findn a close gas station
#by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator =  gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON Empty***")
        sleep(2.5)
        print("        Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Gas Tank on Low, searching for nearest gas station")
        sleep(2.5)
        print("The Closest gas station is",listOfGasStations(),"",milesToGasStationsLow,"Miles away.")
    elif gasLevelIndicator == "Qaurter Tank":
        print("Quarter Gas Tank, searching for nearest gas station")
        sleep(2.5)
        print("The Closest gas station is",listOfGasStations(),"",milesToGasStationsQuartertank,"Miles away.")
    elif gasLevelIndicator == "Half Tank":
         print("Gas Tank is at half")
    else:
        print("Gas Tank is full")
        

print("********************************************************************************")

print("           Weather Branch\n")



#Create a function that randomly chooses the weather form a list
def weather():
    weatherForecast = ["snowy", "blizzard", "rainy", "foggy", "windy", "icy", "sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call the weather() once the VRS(Vehicle Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
            "Weather conditions")
        sleep(0.5)
        print("VRS has been engaged only allowing you to drive 40pmh.")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forceast of",weatherAlert,
            "weather conditions.")
        sleep(0.5)
        print("VRS has been engaged only allowing you to drive 30pmh.")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
            "weather conditions.")
        sleep(0.5)
        print("VRS has been engaged only allowing you to drive 60pmh.")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
            "weather conditions.")
        sleep(0.5)
        print("VRS has been engaged only allowing you to drive 60pmh.")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
            "weather conditions.")
        sleep(0.5)
        print("VRS has been engaged only allowing you to drive 70pmh.")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forceast of",weatherAlert,
            "weather conditions.")
        sleep(0.5)
        print("VRS has been engaged only allowing you to drive 30pmh.")
    else: 
        print("\nNational Weather Service has no update for alarms today because of the forceast of",weatherAlert,
            "weather conditions.")
        sleep(0.5)
        print("VRS has been disengaged.")
   
    
  

    






gasLevelAlert()


vehicleResponseSystem()


