#imports
import random
from pyscript import document
    #possible things it can pick (must be a string/text)
badOptions = {0:"WHY!!!! NEVER EVER!!! NO!!!!!",1:"Why the hell would that be a good idea? NO", 2:"NO NO NO NO NO NO NO NO", 3:"No no no no no no", 4:"Please god no", 5:"No please no", 6:"No, just no", 7:"Hell no", 8:"Maybe not", 9:"I have one word: no", 10:"I have two words: no.\nHang on that is only one", 11:"No"}
goodOptions = {0:"YES YES ABSOLUTLY WHY WOULD YOU NOT!!!!!",1:"When wouldn't that be a bad idea? Yes all the way!",2:"YES YES YES YES YES YES",3:"Yes yes yes yes yes yes yes",4:"Please that would be... A YES",5:"what stopping you? Yes",6:"nothing bad could happen. Yes",7:"God yes",8:"Why not?",9:"I have two words: Yes.\nWait that's one...",10:"I have one word: Yes",11:"Yes"}
#don't change these variables
intensity = 0
yesOrNo = 0

#functions
def decide():
    if yesOrNo:
        return(goodOptions[intensity])
    else:
        return(badOptions[intensity])
    
#where the magic happens
def run8ball(event):
    repeatNum = 0
    asktemp = document.querySelector('#ask')
    ask = asktemp.value
    intensity = random.randint(0, 10)
    yesOrNo = random.randint(0,1)
    ask = input("Ask a yes or no question and we, The Counsil will decide\n→")
    if ask == "dev":
        print("Our almighty creator, we shall tell you our random decision: intensity: ",  intensity, ", yes or no: ", yesOrNo)
    else:
        if yesOrNo:
            reply = goodOptions[intensity]
        else:
            reply = badOptions[intensity]
        reply_div = document.querySelector("#8ballreply")
        reply_div.innerText = reply
