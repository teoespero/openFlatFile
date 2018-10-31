# Teo Espero
# BS Cloud and Systems Administration
# Western Governors University

# declare a global array variable
fruit = ["banana", "apple", "pineapple", "kiwi"]


def getChoice():
    # this function actually captures user input
    # on what they want to do with the fruit list

    pick = input("Enter action: ")
    return pick

def errorMsg(msg):
    # a generic error message display
    print(msg)


def addFruit(fruitParam = ""):
    # constitutes the add fruit function

    more = True
    global fruit
    again = "Y"
    found = False
    newFruit = fruitParam

    # Ask for fruits
    while more:
        if len(newFruit) < 1:
            newFruit = input("Add a new fruit: ")

        # check if the fruit being added is already in the list
        # instead of comparing the fruit by element
        # we are using the 'in' keyword
        if newFruit.casefold() in fruit:
            # if YES say its in the list
            print("Fruit already in list!!!")
            found = True
        else:
            # if NO, add it to the list
            fruit.append(newFruit.casefold())

        # ask for more fruits
        again = input("Add another fruit (Y/N)? ")
        if again.casefold() != "y":
            more = False
        newFruit = ""


def printFruits():
    # constitutes the list fruit function
    global fruit
    print("\nFruit list")
    print("----------")

    count = 0
    for ctr in fruit:
        count = count + 1
        print(str(count) + ". " + ctr)
    print("----------")

    # get a fruit count
    print("Total fruits: ", count)


def remFruit():
    # allows you to remove a fruit

    global fruit
    what = input("Which fruit to remove? ")
    what = what.lower()

    # check if the fruit exist
    if what in fruit:
        # asks for confirmation

        sure = input("This process cannot be undone. Continue (y/n)? ")
        sure = sure.lower()
        if sure in "yn":
            if sure == "y":
                position = fruit.index(what)
                del fruit[position]
        else:
            errorMsg("Invalid. y or n only")
    else:
        # if the user tries to remove a fruit that
        # is not on the list, it will suggest that we can add it
        errorMsg("The fruit " + what + " does not exist in the list.")

        # confirm if the user wants to add it
        addIt = input("Would you like to add it (y/n)? ")
        addIt = addIt.lower()
        if addIt in "yn":
            if addIt == "y":
                addFruit(what)
        else:
            errorMsg("Invalid. y or n only")


def doQuit():
    # quit the application

    yesOrNo = input("You sure you want to quit (y/n)? ")
    yesOrNo = yesOrNo.lower()
    if yesOrNo in "yn":
        if yesOrNo == "y":
            return False
        else:
            return True
    else:
        errorMsg("Invalid. y or n only")
        return True


def doAction(myAction):
    # process the action taken by the user
    if myAction == 1:
        addFruit()
        return True
    elif myAction == 2:
        remFruit()
        return True
    elif myAction == 3:
        printFruits()
        return True
    else:
        return doQuit()


def showMenu():
    print("--------------------------------")
    print("Menu functions")
    print("--------------------------------")
    print("[1] - Add a fruit")
    print("[2] - Remove a fruit")
    print("[3] - Print the fruit list")
    print("[4] - Quit")
    print("--------------------------------")




# Begin - Main program

looper = True
while looper:
    showMenu()
    userChoice = getChoice()
    if userChoice not in ("1234"):
        errorMsg("Invalid Action.")
    else:
        looper = doAction(int(userChoice))

# End - Main program