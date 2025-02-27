#imports
import random
import math
from modules import randPick
from pyscript import document
#variable configuration
    #possible things it can pick (must be a string/text)
Modifiable = [""]
AllFren = ["Rylan", "Jett", "James", "Izzy", "Emily", "Callum"]
SchoolFrenGroup = ["Rylan", "Jett", "Emily", "Callum"]

listSaves = {0:Modifiable, 1:AllFren, 2:SchoolFrenGroup}
listSaveSelect = 2
    #amount of peices of text it picks
amountPick = 1
amountNumber = 1
lowNumber = 1
highNumber = 10
numStep = 1
    #will it remove picked text after each go (true or false, case sensitive)
rouletteMode = False
    #number settings
def manyRandInt(
    lowNumber: int = 1,
    highNumber: int = 10,
    amountNumber: int = 2,
    numStep: int = 1
):
    import random
    allNum = []
    trueAllNum = {}
    repeatNum = 0
    for i in range(1, (amountNumber + 1)):
             #number randomiser
        mystery = random.randrange(lowNumber, highNumber, numStep)
        print(mystery)
        allNum.append(mystery)

    for i in range(lowNumber, (highNumber + 1)):
        tempCounter = allNum.count((lowNumber) + repeatNum)
        if tempCounter != 0:
            trueAllNum.update({(lowNumber + repeatNum) : tempCounter})
    
        repeatNum += 1
    return(trueAllNum)

def runNumberGen(event):
    
        #amount of numbers that get chosen
    amountNumber = document.querySelector('#amountNum')
        #if it'll pick numbers  (true or false, case sensitive)
    number = True
        #lowest number possible
    lowNumber = document.querySelector('#lowNum')
        #highest number possible
    highNumber = document.querySelector('#highNum')
        #number gap between options for random numbers (e.g: 1 = all numbers, 10 = multiples of 10)
    numStep = document.querySelector('#numStep')
#don't change these variables
    canPick = listSaves[listSaveSelect]
    allMystery = []
    repeatNum = 0
    trueAllMystery = {}
    allPick = []
    trueAllPick = {}
    savePick = canPick.copy()
#where the magic happens for numbers
    #repeating loop
    numbersAre = "The numbers are: " + randPick.manyRandInt(lowNumber, highNumber, amountNumber, numStep)
    numberOut = document.querySelector('#numOut')
    numberOut.innterText = numbersAre

