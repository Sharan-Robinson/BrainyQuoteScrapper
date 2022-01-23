#this is going to be where the prompt is going to be display on the command line.
from index import newlist
from SearchandGrabdef import leechQnA, loading
import random

def getvalue(value, dictionary):
    for i, j in dictionary.items():
        if value == i:
            return j
    return "not found"




numdict = dict(zip(range(1, len(newlist) + 1), newlist))


while True:
    sameline = 0
    for i,j in numdict.items():
        if sameline < 9:
            print(str(i) + "." + j + " ", end="", flush=True)
            sameline += 1

        else:
            print(str(i) + "." +j)
            sameline  = 0

    print("\nEnter 0 to quit")
    num = input("Please enter a number corresponding to the topic you would like a quote from:")

    try:
      if int(num) == 0:
            exit()
    except ValueError:
        print("Please enter a number instead, Try Again.")
        keypressed = False
        while (keypressed != True):
            keypress = input("Press Enter to continue")

            if keypress == "":
                keypressed == True
                break
            else:
                continue
        continue




    givevale = getvalue(int(num), numdict)
    if givevale == "not found":
        print("This does not seem to be a valid number, Please try again.")
        keypressed = False
        while (keypressed != True):
            keypress = input("Press Enter to continue")

            if keypress == "":
                keypressed == True
                break
            else:
                continue
        continue
    Quotes, Authors, dict = leechQnA(givevale)
    randnum = random.SystemRandom()

    num1 = randnum.randint(0,len(Quotes))

    print(f"{Quotes[num1]}" + "\n" +
          f"{Authors[num1]}")
    keypressed = False
    while (keypressed != True):
        keypress = input("Press Enter to continue")

        if keypress == "":
            keypressed == True
            break

        else:
            continue


