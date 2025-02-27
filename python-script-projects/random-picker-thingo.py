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

    #will it remove picked text after each go (true or false, case sensitive)
rouletteMode = False
    #number settings
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

