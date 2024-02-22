print("*******************************")
print("Gasoline Branch\n\n")

#Import Libraries HEre
import random
from time import sleep

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
        
    





gasLevelAlert()




