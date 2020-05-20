import random

money = 100

#Write your game of chance functions here

#Coin Flip
def coinFlip(bet, betAmount):
    #Checking if bet is above 0
    if betAmount <= 0:
        print("")
        print("================================================")
        print("Your bet should be above 0.")
        print("================================================")
        print("")
        return 0

    #Checking if not above actual allowance
    elif betAmount > money:
        print("")
        print("================================================")
        print("Your bet should not be above your allowance.")
        print("================================================")
        print("")
        return 0


    print("")
    print("================================================")
    print("Lets flip the coin!")
    coin = random.randint(1, 2)
    heads = 1
    tails = 2
    if coin == tails:
        print ("Tails!")
        if bet == "tails":
            print ("You win! And you won " + str(betAmount) + " quid!")
            print("================================================")
            return betAmount
        else:
            print ("You Lose! And you lost " + str(betAmount) + " quid!")
            print("================================================")
            return -betAmount
    else:
        print ("Heads!")
        if bet == "heads":
            print ("You win! And you won " + str(betAmount) + " quid!")
            print("================================================")
            return betAmount
        else:
            print ("You Lose! And you lost " + str(betAmount) + " quid!")
            print("================================================")
            return -betAmount

#Cho - Chan
def choChan(bet, betAmount):
    #Checking if bet is above 0
    if betAmount <= 0:
        print("")
        print("================================================")
        print("Your bet should be above 0.")
        print("================================================")
        print("")
        return 0

    #Checking if not above actual allowance
    elif betAmount > money:
        print("")
        print("================================================")
        print("Your bet should not be above your allowance.")
        print("================================================")
        print("")
        return 0

    print("")
    print("================================================")
    print("Lets play Cho Chan!")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("You guessed " + bet + ".")
    if total % 2 == 0 and bet == "even":
        print("The total was " + str(total) + ". So you Win " + str(betAmount) + " quid!")
        print("================================================")
        return betAmount
    elif total % 2 == 1 and bet == "odd":
        print("The total was " + str(total) + ". So you Win " + str(betAmount) + " quid!")
        print("================================================")
        return betAmount
    else:
        print("But the total was " + str(total) + ". So you Lose " + str(betAmount) + " quid!")
        print("================================================")
        return -betAmount

#Higher Card Wins
def topTrump(betAmount):
    #Checking if bet is above 0
    if betAmount <= 0:
        print("")
        print("================================================")
        print("Your bet should be above 0.")
        print("================================================")
        print("")
        return 0

    #Checking if not above actual allowance
    elif betAmount > money:
        print("")
        print("================================================")
        print("Your bet should not be above your allowance.")
        print("================================================")
        print("")
        return 0

    print("")
    print("================================================")
    print("Lets see who has the higher card!")
    myCard = random.randint(1, 13)
    cmpCard = random.randint(1, 13)
    if myCard == 13:
        print("My Card is a King.")
        if cmpCard == 13:
            print("And their card is a King.")
        elif cmpCard == 12:
            print("And their card is a Queen.")
        elif cmpCard == 11:
            print("And their card is a Jack.")
        else:
            print("And their card is a " + str(cmpCard) + ".")
    elif myCard == 12:
        print("My card is a Queen")
        if cmpCard == 13:
            print("And their card is a King.")
        elif cmpCard == 12:
            print("And their card is a Queen.")
        elif cmpCard == 11:
            print("And their card is a Jack.")
        else:
            print("And their card is a " + str(cmpCard) + ".")
    elif myCard == 11:
        print("My card is a Jack")
        if cmpCard == 13:
            print("And their card is a King.")
        elif cmpCard == 12:
            print("And their card is a Queen.")
        elif cmpCard == 11:
            print("And their card is a Jack.")
        else:
            print("And their card is a " + str(cmpCard) + ".")
    else:
        print("My card is a " + str(myCard) + ".")
        print("And their card is a " + str(cmpCard) + ".")
    if myCard > cmpCard:
        print("So you win " + str(betAmount) + " quid!")
        print("================================================")
        return betAmount
    elif myCard < cmpCard:
        print("So you lose " + str(betAmount) + " quid!")
        print("================================================")
        return -betAmount
    else:
        print("So its a tie!")
        print("================================================")
        return 0

#Roulette
def roulette(bet, betAmount):
    #Checking if bet is above 0
    if betAmount <= 0:
        print("")
        print("================================================")
        print("Your bet should be above 0.")
        print("================================================")
        print("")
        return 0

    #Checking if not above actual allowance
    elif betAmount > money:
        print("")
        print("================================================")
        print("Your bet should not be above your allowance.")
        print("================================================")
        print("")
        return 0

    print("")
    print("================================================")
    print("Lets play Roulette!")
    randNum = random.randint(0, 37)
    if randNum == 37:
        print("The ball landed on 00.")
    else:
        print("The ball landed on " + str(randNum) + ".")

    if randNum != 0 and randNum % 2 == 0 and bet == "even":
        print("You guessed " + str(bet) +".")
        print("And the result is " + str(randNum) +". So you won "+str(betAmount)+" quid!")
        print("================================================")
        return betAmount
    elif randNum != 37 and randNum % 2 == 1 and bet == "odd":
        print("You guessed " + str(bet) +".")
        print("And the result is " + str(randNum) +". So you won "+str(betAmount)+" quid!")
        print("================================================")
        return betAmount
    elif bet == randNum:
        print("You guessed " + str(bet) +".")
        print("And the result is " + str(randNum) +". So you won "+str(betAmount * 20)+" quid!")
        print("================================================")
        return betAmount * 20
    else:
        print("You guessed " + str(bet) +".")
        print("And the result is " + str(randNum) +". So you lost "+str(betAmount)+" quid. Oh no!")
        print("================================================")
        return -betAmount

#Call your game of chance functions here
money += coinFlip("heads", 0)
money += coinFlip("heads", 20)
money += choChan("even", 0)
money += choChan("even", 20)
money += topTrump(0)
money += topTrump(20)
money += roulette("32", 0)
money += roulette("odd", 20)
money += roulette("even", 20)
money += roulette("32", 20)
print(money)
