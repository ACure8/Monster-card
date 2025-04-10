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
#New error that if you don't go back to privious selection then exit you won't be able to end this program
def main():
    user_choice = ""
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
        elif user_choice == None:
            exit()

#add new cards to the catalogue Once the user has added a card, the program should display the card that
#has been added, and check with the user whether the details are correct, or if
#they want to make a change.
def add():
    eg.msgbox("This is Add Card")
    name = eg.enterbox("What do you want to name the monster?", "Add Card")
    while name.title() in Cards.keys() or name in Cards.keys():
        eg.msgbox(f"{name} already exists, try again", "error")
        name = eg.enterbox("What do you want to name the monster?", "Add Card")
    strength = eg.integerbox("How much strength do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) #made a limiter for highest and lowest
    speed = eg.integerbox("How much speed do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
    stealth = eg.integerbox("How much stealth do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
    cunning = eg.integerbox("How much cunning do you want to give the monster?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1)
    new_dict = { # Makes the data so if the player wants to change it then they can
        name : {
            "Strength" : strength,
            "Speed" : speed,
            "Stealth" : stealth,
            "Cunning" : cunning
        }
    }
    while eg.buttonbox(f"Are you happy with this or do you want to make some changes?\n{new_dict}", "Add Card", ["Change", "Done"]) == "Change": #This will loop till you're satisfied though it's now working
        new_name = eg.enterbox(f"What name do you want for the monster instead of {name}", "Add Card")
        while new_name.title() in Cards.keys() or new_name in Cards.keys():
            eg.msgbox(f"{new_name} already exists, try again", "error")
            new_name = eg.enterbox(f"What name do you want for the monster instead of {name}", "Add Card")
        new_strength = eg.integerbox(f"How much strength do you want to give the monster instead of {strength}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1)
        new_speed = eg.integerbox(f"How much speed do you want to give the monster instead of {speed}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
        new_stealth = eg.integerbox(f"How much stealth do you want to give the monster instead of {stealth}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
        new_cunning = eg.integerbox(f"How much cunning do you want to give the monster instead of {cunning}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1)
        name = new_name
        strength = new_strength
        speed = new_speed
        stealth = new_stealth
        cunning = new_cunning

        new_dict = { # I used the same name as it replaces the previous data
            name : {
                "Strength" : strength,
                "Speed" : speed,
                "Stealth" : stealth,
                "Cunning" : cunning
            }
        }
        if eg.buttonbox(f"Are you happy with this or do you want to make some changes?\n{new_dict}", "Add Card", ["Change", "Done"]) == "Done":
            break
    Cards.update(new_dict) #finally when you're done changeing it, the dict in then added into the 'Cards' dict
    eg.msgbox(Cards)
    user_choice = eg.buttonbox("Do you want to return to Main screen? or end this program(Exit)", "Add Card", ["Main", "Exit"])
    if user_choice == "Main":
        main()
    elif user_choice == "Exit":
        exit()

#Allow the user to search the catalogue for an existing monster card, check that
#the monster’s details are correct, and make changes if necessary.
def search():
    eg.msgbox("This is Search")
    card = eg.choicebox("Pick which one you want to see:", "Search", choices = list(Cards)) #cancel does not work
    if card == None:
        main()
    elif card:
        leave = eg.buttonbox(f"{card}:\n{Cards[card]}","Search", ["Change", "Main", "Exit"])
    if leave == "Change":
        new_name = eg.enterbox(f"What name do you want for the monster instead of {card}", "Add Card")
        while new_name.title() in Cards.keys() or new_name in Cards.keys():
            eg.msgbox(f"{new_name} already exists, try again", "error")
            new_name = eg.enterbox(f"What name do you want for the monster instead of {card}", "Add Card")
        new_strength = eg.integerbox(f"How much strength do you want to give the monster instead of {Cards[card]['Strength']}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1)
        new_speed = eg.integerbox(f"How much speed do you want to give the monster instead of {Cards[card]['Speed']}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
        new_stealth = eg.integerbox(f"How much stealth do you want to give the monster instead of {Cards[card]['Stealth']}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1) 
        new_cunning = eg.integerbox(f"How much cunning do you want to give the monster instead of {Cards[card]['Cunning']}?(minimum is 1 and max is 25)", "Add Card", upperbound = 25, lowerbound = 1)
        del Cards[card]
        Cards[new_name] = {
            "Strength" : new_strength,
            "Speed" : new_speed,
            "Stealth" : new_stealth,
            "Cunning" : new_cunning
        }
        eg.msgbox(Cards)
    elif leave == "Main":
        main()
    else:
        exit()

#Delete a monster card from the catalogue.
def delete():
    eg.msgbox("This is Delete Card")
    while True:
        delete_card = eg.choicebox("Pick which one you want to delete:", "Delete Card", choices = list(Cards)) #cancel does not work
        if delete_card:
            if eg.ccbox("Are you sure?", "Delete Card"):  # show a Continue/Cancel dialog
                delete = Cards.pop(delete_card)
                eg.msgbox(Cards)
        else:
            main()

#Output the full monster card catalogue to Python Shell (to allow for it to be printed out).
def cards():
    eg.msgbox("This is Catalogue")
    print(Cards)
    eg.msgbox("Check python shell")
    main()

main() #this will start the program