import random
#creates a list
cards = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
def main():
    global card1
    global card2
    #pulls 2 random items from the list and stores them as card1 and card2
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    print(f"Card 1 is {card1} and card 2 is {card2}")
    #checks to make sure that the cards are not the same
    while card1 == card2:
        card2 = random.choice(cards)
    else:
        card2 = card2
        card3 = (f"{card1}/{card2}")
    #takes the value of card3 and then puts it into divider()
    divided = divider(card3)

    #Shows all the outputs based on various returns
    if divided == ValueError:
        print("There was a value error")
    if divided == ZeroDivisionError:
        print("You cannot divide by 0")
    else:
        print (divided)

def divider(divide):
    #attempts to convert all the numbers to integers 
    #if not able to then will return a valueerror
    try:
        divide = divide.split("/")
        card4 = int(divide[0])
        card5 = int(divide[1])
    except:
        return ValueError
    #Incase the denominator is 0
    if card5 == 0:
        return ZeroDivisionError
    if card4 > card5:
        return ValueError
    else:
        Divide = (card4/card5)
        return Divide

if __name__ == "__main__":
    main()
