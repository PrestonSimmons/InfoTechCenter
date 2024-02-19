print("*******************************")
print("Gasoline Branch\n\n")

#Import Libraries HEre
import random

1 usage
def gaslevelGauge():
    gasLevelList = ["Empty" "Low" "Quater Tank" "Half Tahnk" "Three Quarter Tank" "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

print(gasLevelGauge())