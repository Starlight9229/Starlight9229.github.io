def fromListMerge(
    listIn: list,
    count: int,
    rouletteMode: bool = 0
):
    import random
    allPick = []
    trueAllPick = {}
    savePick = listIn.copy()
    repeatNum = 0
    if(listIn[0] == ""):
        print("Random list picker failed due to it being empty")
    else:
        if rouletteMode:
            repeatNum = 0
            if count > len(listIn):
                count = len(listIn)
            pickCount = len(listIn)
    
            for i in range(1, (count + 1)):
                mystery = random.randint(0, (len(listIn) - 1))
                allPick.append(listIn[mystery])
                listIn.pop(mystery)
        
   
            for i in range(0, pickCount):
        
                tempCounter = allPick.count(savePick[i])
        
                if tempCounter != 0:
                    trueAllPick.update({savePick[i]:tempCounter})
        #where the magic happens for text (not roulette mode)
        repeatNum = 0
        if rouletteMode == False:
            for i in range(1, (count + 1)):
                mystery = random.randint(0, (len(listIn) - 1))
                allPick.append(listIn[mystery])
        
            for i in range(0, (len(listIn))):
                tempCounter = allPick.count(listIn[i])
                if tempCounter != 0:
                    trueAllPick.update({listIn[i]:tempCounter})
    return(trueAllPick)

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

def manyFromList(
    listIn: list,
    count: int,
    rigged: int = -1
):
    import random
    truePickRand = ""
    for i in range(1, (count + 1)):
        if rigged > -1:
            truePickRand = truePickRand + listIn[rigged]
        else:
            pickRand=random.randint(0, (len(listIn)-1))
            truePickRand = truePickRand + listIn[pickRand]
    if truePickRand == "":
        return ""
    return truePickRand

def fromList(
    listIn: list,
    rigged: int = -1
):
    import random
    if rigged > -1:
        return listIn[rigged]
    else:
        return listIn[random.randint(0, len(listIn)-1)]