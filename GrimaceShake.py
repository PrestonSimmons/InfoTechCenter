print("*******************************")
print("Gasoline Branch\n\n")

#Import Libraries HEre
import random

#Function that list Gas Levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quater Tank","Half Tahk","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function thats lists Gas Stations,m randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Marathon", "Circle K","Mobile","Costco","Meijers","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby


print(gasLevelGauge())
print(listOfGasStations())