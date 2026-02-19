from section1 import Section1
from section2 import Section2
from games import Games
import random
import platform
import os

#initiatilizing the classes
section1 = Section1()
section2 = Section2()
games = Games()

#to clear screen no matter platform for its terminal
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

#well.. its the intro
def intro():
    introMenu = ["Hello! and welcome to my game!",
                 "The goal of this program is to build your 'funny' muscle."]
    return introMenu

#simple function to get user info while testing to see if its valid
def getUserString(phrase,answers):
    while True:
        userInput = input(phrase+"\n-->")
        if userInput in answers:
            return userInput
        print("please enter one of the provided answers and try again\n")

#simple function to print a list on each line
def printList(list):
    for i in list:
        print(i)

#formats the menu
def mainMenu():
    clear()
    titles = [games.getTitle(),section1.getTitle(),section2.getTitle()]
    print("===============================")
    for i in titles:
        printList(i)
    print("===============================")
    secChoice = getUserString("Welome to the main menu. Which section would you like to dive into? (just enter the section number)",("0","1","2"))
    clear()
    if secChoice == "1":
        section1Options()
    elif secChoice == "0":
        justTheGames()
    elif secChoice == "2":
        section2Options()
    

#incase you need to know how many items are in a list
def getAmountInList(lst):
    num = 0
    for i in lst:
        num += 1
    return num

#logic for if there is no game in the section/technique
def logicTechniqueOption(chapter,homework):
    inTechnique = True
    print(chapter[0])
    while inTechnique:
        gameChoice = getUserString("Would you like to review the chapter [r], review basic homework [h], ([m] for menu) \n([b] for back)",("r","h","m","b"))
        clear()
        if gameChoice == 'r':
            printList(chapter)
        elif gameChoice == 'h':
            printList(homework)
        elif gameChoice == 'm':
            return mainMenu()
        elif gameChoice == 'b':
            inTechnique = False

#this is the technique logic for every other section (since they have games)
def logicTechGameOption(chapter,homework,game):
    inTechnique = True
    print(chapter[0])
    while inTechnique:
        gameChoice = getUserString("Would you like to review the chapter [r], review basic homework [h], or play this chapters game? [g] ([m] for menu)\n([b] for back)",("r","h","g","m","b"))
        clear()
        if gameChoice == 'r':
            printList(chapter)
        elif gameChoice == 'h':
            printList(homework)
        elif gameChoice == 'm':
            return mainMenu()
        elif gameChoice == 'g':
            game()
            clear()
            print(chapter[0])
        elif gameChoice == 'b':
            inTechnique = False

#choose games as randomly based off the list of games given
def randDrills(gamesList):
    gameToPlay = random.choice(gamesList)
    gameToPlay()
    return

#Menu for just doing games
def justTheGames():
    clear()
    print()
    printList(games.getTitle())
    printList(games.getContents())
    techChoice = getUserString("Great! Which game would you like to go into? (just enter the game number)\n[m] for menu",("m","1","2","0","3"))
    clear()
    if techChoice == "1":
        describingGame()
    elif techChoice == "m":
        mainMenu()
    elif techChoice == "2":
        metaphorGame()
    elif techChoice == "0":
        exagerateGame()
    elif techChoice == "3":
        stickLabelGame()
    return justTheGames()

#here is the menu for while you're in the first section
def section1Options():
    print()
    printList(section1.getTitle())
    printList(section1.getContents())
    techChoice = getUserString("Great! Which technique would you like to go into? (just enter the technique number)",("1","2","3"))
    clear()
    if techChoice == "1":
        logicTechniqueOption(section1.getCh1(),section1.getHome())
    elif techChoice == "2":
        logicTechniqueOption(section1.getCh2(),section1.getHome())
    elif techChoice == "3":
        logicTechniqueOption(section1.getCh3(),section1.getHome())
    return section1Options()



#here is the menu for while you're in the second section
def section2Options():
    inTechnique = True
    print()
    printList(section2.getTitle())
    choice = getUserString("Do you want to choose the chapter [c] or have random drills? [d](games) \n[m] for menu",('c','d','m'))
    if choice == 'c':
        printList(section2.getContents())
        techChoice = getUserString("Great! Which technique would you like to go into? (just enter the technique number)",("4","5","6","7","8","9","10"))
        clear()
        if techChoice == "4":
            logicTechGameOption(section2.getCh4(),section2.getCh4Home(),describingGame)
        if techChoice == "5": 
            logicTechGameOption(section2.getCh5(),section2.getCh5Home(),metaphorGame)
    elif choice == 'd':
        inGames = True
        while inGames:
            randDrills([describingGame,metaphorGame,exagerateGame,stickLabelGame])
            if getUserString("[m] for menu. [enter] for another random game",(""," ","m")) == 'm':
                inGames = False
    elif choice == 'm':
        mainMenu()

    return section2Options()


def gameLogicLayout(chapterExam,addExamMethod,gameDesc,instruction):
    clear()
    wordsList = chapterExam
    for i in gameDesc:
        print(i)
    input("press enter when you're ready")
    playing = True
    while playing:
        randomWord = random.choice(list(wordsList.keys()))
        print(instruction,randomWord+"?")
        addedExample = input("--> ")
        addExamMethod(randomWord,addedExample)
        gameplay = getUserString("Again? ([enter] to continue) or ([n] for no) or ([e] for some examples)",("y","n",""," ","e"))
        if gameplay == 'n':
            playing = False
        elif gameplay == 'e':
            print("Here are some examples")
            for i in chapterExam[randomWord]:
                print("* "+i)
            if getUserString("Again? ([enter] to contiue) or ([n] for no)",("y","n",""," ")) =='n':
                playing = False
    return

#this is ch 4's game (in section 2)
def describingGame():
    gameLogicLayout(section2.getCh4Exam(),section2.addExamples4,["Hello and welcome to the 'painting more with details' game!",
                                                                 "Your goal is to write down another way to decribe something in a more colorful way!"],
                                                                 "What's another way to describe")
    return

#ch 5's game
def metaphorGame():
    gameLogicLayout(section2.getCh5Exam(),section2.addExamples5,["Hello and welcome to the 'painting with metaphors' game!",
                                                               "Your goal is with the given metaphor, you break it and stretch it get a laugh!",
                                                               "It'll make sense.."],
                                                               "Fill in the blank: ")
    return

#ch 6 game
def exagerateGame():
    gameLogicLayout(games.getExagerate(),games.addToExagerate,["Hello and welcome to the 'exagerate' game!",
                                                               "I know... It's the worst game title, but as the game suggests",
                                                               "You'll literally just exagerate the given statement"],
                                                               "Exagerate the statement: ")
    return

def stickLabelGame():
    gameLogicLayout(games.getStickLabel(),games.addToStickLabel,["Hello and welcome to the 'stick a label on it' game!",
                                                                 "Your goal is to simplify the object/statement into something funny (name it)",
                                                                 "It's funny to label something with certain characteristics"],
                                                                 "Label this: ")
        
        

    
    

def main():
    clear()
    printList(intro())
    mainMenu()

if __name__ == '__main__':
    main()