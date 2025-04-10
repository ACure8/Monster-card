import easygui as eg #This will make it easy for me when I don't want to write the whole word

Cards = { #These are the cards that already exist in the catalogue
    "Stoneling": {
        "Strength" : 7,
        "Speed" : 1,
        "Stealth" : 25,
        "Cunning"  : 15
    },
    "Vexscream": {
        "Strength" : 1,
        "Speed" : 6,
        "Stealth" : 21,
        "Cunning"  : 19
    },
    "Dawnmirage": {
        "Strength" : 5,
        "Speed" : 15,
        "Stealth" : 18,
        "Cunning"  : 22
    },
    "Blazegolem": {
        "Strength" : 15,
        "Speed" : 20,
        "Stealth" : 23,
        "Cunning"  : 6
    },
    "Websnake": {
        "Strength" : 7,
        "Speed" : 15,
        "Stealth" : 10,
        "Cunning"  : 5
    },
    "Moldvine": {
        "Strength" : 21,
        "Speed" : 18,
        "Stealth" : 14,
        "Cunning"  : 5
    },
    "Vortexwing": {
        "Strength" : 19,
        "Speed" : 13,
        "Stealth" : 19,
        "Cunning"  : 2
    },
    "Rotthing": {
        "Strength" : 16,
        "Speed" : 7,
        "Stealth" : 4,
        "Cunning"  : 12
    },
    "Froststep": {
        "Strength" : 14,
        "Speed" : 14,
        "Stealth" : 17,
        "Cunning"  : 4
    },
    "Wispghoul": {
        "Strength" : 17,
        "Speed" : 19,
        "Stealth" : 3,
        "Cunning"  : 2
    }
}

selection = { #This will be used to make navagating easier
    "Add Card" : "add",
    "Search" : "search",
    "Delete Card" : "delete",
    "Catalogue" : "cards",
}


#A main screen to navagate the options, I also moved it to the top to remove the error of "local variable 'selection' referenced before assignment"
def main():
    user_choice = eg.buttonbox("What do you want to do?", "Main", choices = list(selection.keys())) #I got the keys of the dictonary and turned them into a list so the choices will show "Add card", "Search", etc
    if user_choice:
        if selection[user_choice] == "add":
            add()
        elif selection[user_choice] == "search":
            search()
        elif selection[user_choice] == "delete":
            delete()
        elif selection[user_choice] == "cards":
            cards()

#add new cards to the catalogue Once the user has added a card, the program should display the card that
#has been added, and check with the user whether the details are correct, or if
#they want to make a change.
def add():
    eg.msgbox("this is Add Card")
    name = eg.enterbox("What do you want to name the monster?", "Add Card")
    strength = eg.integerbox("How much strength do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) #made a limiter for highest and lowest
    speed = eg.integerbox("How much speed do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
    stealth = eg.integerbox("How much stealth do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
    cunning = eg.integerbox("How much cunning do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1)

    user_choice = eg.buttonbox("Do you want to return to Main screen? or end this program(Exit)", "Add Card", choices = list(selection.keys))
    if user_choice == "Main":
        main()

#Allow the user to search the catalogue for an existing monster card, check that
#the monster’s details are correct, and make changes if necessary.
def search():
    eg.msgbox("this is search")

#Delete a monster card from the catalogue.
def delete():
    eg.msgbox("this is delete")

#Output the full monster card catalogue to Python Shell (to allow for it to be printed out).
def cards():
    eg.msgbox("this is Catalogue") #I'm tagging the code under so the error doesn't interupt the rest of the code
#    words = ""
 #   for i in list(Cards.keys):
  #      words += f"{i}:\n{Cards[i]["Strength"]}\n{Cards[i]["Speed"]}\n{Cards[i]["Stealth"]}\n{Cards[i]["Cunning"]}\n" #I got error here saying "f-string:unmached '[' SyntaxError"
   # print(words)

main() #this will start the program