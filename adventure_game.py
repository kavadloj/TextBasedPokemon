# Jonah Kavadlo
from random import *
from pokemon import Pokemon
from player import Player

def main():
    # Intro
    input("Welcome to the wonderful world of Pokemon! Press enter after each line to proceed through the game. When prompted with decisions, enter your choice.") 
    input("\nYou are Dr. Fuji, a researcher for the infamous Team Rocket. Two years ago, you created the legendary Pokemon, Mewtwo. Not long after, it violently escaped! Now, you've been sent to the depths of the Cerulean Cave to capture it and fix your mistake.")
    input("\nYou have invented a PSI detector, which will tell you how far you are from Mewtwo by detecting its psychic aura.")
    input("\nYou've also brought your trusty Charizard and some supplies in case you encounter any dangerous Pokemon.")
    input("\nWhen a wild Pokemon appears, you can either attack it, try to run away, or catch it. Be warned: failure to run or catch the Pokemon will result in it landing a free attack.")
    
    choice = input("\nDo you dare enter the cave? (y/n) ")
    while choice != "y" and choice != "Y":
        choice = input("Team Rocket will have your head if you don’t return with Mewtwo! So, will you enter the cave? (y/n) ")
    
    # Pokemon species (attack stats adjusted for damage rolls)
    charizard = Pokemon("Charizard", 46, 100, 100, "Flamethrower", "Your trusty companion.")
    mewtwo = Pokemon("Mewtwo", 76, 100, 130, "Psystrike", "It's the strongest Pokemon of them all!")
    golduck = Pokemon("Golduck", 36, 80, 85, "Water Pulse", "It looks confused...")
    magikarp = Pokemon("Magikarp", 0, 20, 80, "Flail", "It's the weakest Pokemon of them all!")
    slowbro = Pokemon("Slowbro", 36, 95, 30, "Bubblebeam", "It's a slippery water type!")
    kingler = Pokemon("Kingler", 51, 55, 75, "Crabhammer", "It's a slippery water type!")
    poliwag = Pokemon("Poliwag", 26, 40, 90, "Bubble", "It's a slippery water type!")
    graveler = Pokemon("Graveler", 26, 140, 35, "Rock Throw", "This rock type cave dweller is pretty hardy.")
    primeape = Pokemon("Primeape", 51, 65, 95, "Low Kick", "It looks angry!")
    golbat = Pokemon("Golbat", 26, 90, 105, "Wing Attack", "It's fast!")
    magneton = Pokemon("Magneton", 51, 55, 70, "Tri Attack", "Be careful not to get zapped!")
    chansey = Pokemon("Chansey", 6, 190, 50, "Pound", "It looks nicer than it really is...")
    arbok = Pokemon("Arbok", 36, 60, 80, "Poison Sting", "It looks angry!")
    lickitung = Pokemon("Lickitung", 31, 120, 30, "Lick", "It looks hungry!")
    fearow = Pokemon("Fearow", 51, 65, 100, "Fury Attack", "It looks angry!")
    raichu = Pokemon("Raichu", 36, 60, 110, "Thunderbolt", "Be careful not to get zapped!")
    parasect = Pokemon("Parasect", 36, 60, 30, "Leech Life", "It looks scarier than it really is...")
    sandslash = Pokemon("Sandslash", 51, 75, 65, "Dig", "It looks angry!")
    ditto = Pokemon("Ditto", 10, 55, 55, "Struggle", "It can shapeshift!")
    
    wildPokemon = [mewtwo, golduck, magikarp, slowbro, kingler, poliwag, graveler, primeape, golbat, magneton, chansey, arbok, lickitung, fearow, raichu, sandslash, ditto]
    
    fuji = Player("Fuji", [charizard], [3, 0, 0, 1])
        
    input("\nIt's pitch black. Luckily, your Charizard can light the way with its flames.")
    
    # Game
    gameLength = 10
    while gameLength > 0:
        roll = random()
        if gameLength == 10:
            choice = input("The only way to go is straight. Proceed? (y/n) ")
            while choice != "y" and choice != "Y":
                choice = input("Team Rocket will send you straight to your doom if you don't find Mewtwo! So, will you proceed? (y/n) ")
            
            event(.2, fuji, wildPokemon)
            
        else:
            if gameLength == 1:
                roll = 0
            paths(roll)
            event(roll, fuji, wildPokemon)
        gameLength = gameLength - 1
        
        if gameLength == 2:
            input("Bzzz...")
            input("The PSI detector is buzzing. You're getting close.")
        
        elif gameLength == 1:
            input("BZZ..")
            input("You're almost there!")
        
        if gameLength == 0:
            roll = 10
            input("BZZZZZT!")
            input("The PSI detector is going crazy! Suddenly, you see a pair of bright purple eyes in the dark.")
            input("This is it. The final battle. The ultimate test. Let's see if you can reach your goal!")
            input("Catch Mewtwo or knock it out to win.")
            
            battle(fuji, wildPokemon, roll)
            
            input("Finally, Mewtwo is back in the custody of Team Rocket. You're scared of what they might do with it.")
            input("That kind of psychic potential could be a disaster in the wrong hands.")
            input("But for now, you can finally relax after your tiring adventure.")
            print("The end!\n")
                        
            partyStr = "Ending party: "
            for pokemon in fuji.getParty():
                if pokemon.getName() == "Charizard":
                    partyStr = partyStr + pokemon.getName() + " (" + str(pokemon.getHealth()) + " HP)"
                else:
                    partyStr = partyStr + ", " + pokemon.getName() + " (" + str(pokemon.getHealth()) + " HP)"
            print(partyStr)
            print("Ending inventory: {0} Poke Ball(s), {1} Nugget(s), {2} Master Ball(s), {3} Super Potion(s)".format(fuji.getItem(0), fuji.getItem(1), fuji.getItem(2), fuji.getItem(3)))

def paths(roll):
    if roll <= .4 and roll >= 0:
        choice = input("The only way to go is straight. Proceed? (y/n) ")
        while choice != "y" and choice != "Y":
            choice = input("Team Rocket will send you straight to your doom if you don't find Mewtwo! So, will you proceed? (y/n) ")
    
    elif roll <= .7 and roll > .4:
        choice = input("There's a fork in the tunnel. Do you want to turn left or right? (l/r) ")
        while choice != "l" and choice != "r" and choice != "L" and choice != "R":
            choice = input("Team Rocket won't even give you a choice about your path if you don't find Mewtwo! So, will you go left or right? (l/r) ")
    
    elif roll <= .95 and roll > .7:
        choice = input("You found an underground river. Attempt to swim across? (y/n) ")
        while choice != "y" and choice != "Y":
            choice = input("You'll be swimmin' with the Magikarps either way if you don't find Mewtwo! So, will you swim across or not? (y/n) ")
    
    else:
        input("You've reached a dead end and need to turn back.")

def event(roll, fuji, wildPokemon):
    itemOrBattle = randrange(1, 3)
    # Land event
    if roll >= 0 and roll <= .7:
        
        if itemOrBattle == 1:
            battle(fuji, wildPokemon, roll)
        
        elif itemOrBattle == 2:
            choice = input("The path leads into a small cavern. Look around for items? (y/n) ")
            
            if choice == "y" or choice == "Y":
                getItem(fuji)
            
            else:
                input("Your loss. You might have found something useful.")
                print("")
    # Water event
    elif roll <= .95 and roll > .7:
        input("You begin paddling through the murky water.")
        battle(fuji, wildPokemon, roll)
    # Dead end
    else:
       input("You trek back to the most recent traversable path.")
       print("")
             
def getItem(fuji):
    randomItem = random()
    # Unlucky option
    if randomItem > 0 and randomItem <= .2:
        input("You only found dirt and rocks...")
    # Found Poke Ball
    elif randomItem > .2 and randomItem <= .5:
        input("You found one Poke Ball! You can use it to catch wild Pokemon that you find. It's not always successful, though.")
        fuji.addItem(0)
        input("You have {0} Poke Ball(s).".format(fuji.getItem(0)))
    # Found Nugget
    elif randomItem > .5 and randomItem <= .7:
        input("You found a Nugget! It has no use here, but you can sell it later.")
        fuji.addItem(1)
        input("You have {0} Nugget(s).".format(fuji.getItem(1)))
    # Found Potion
    elif randomItem > .7 and randomItem <= .9:
        input("You found a Super Potion! You can use it to heal an active Pokemon during battle.")
        fuji.addItem(3)
        input("You have {0} Super Potion(s).".format(fuji.getItem(3)))
    # Found Master Ball
    else:
        input("You found a Master Ball! It has a 100% chance to catch any Pokemon that you encounter. Use it wisely.")
        fuji.addItem(2)
        input("You have {0} Master Ball(s).".format(fuji.getItem(2)))
        
    input("You leave the cavern and continue through the cave.")
    print("")
    
def battle(fuji, wildPokemon, roll):
    randomPokemon = randrange(6, len(wildPokemon))
    presentPokemon = wildPokemon[randomPokemon]
    
    # Water Pokemon (Golduck is both)
    if roll <= .95 and roll > .7:
        presentPokemon = wildPokemon[randrange(1, 6)]
    elif roll == 0:
        presentPokemon = wildPokemon[len(wildPokemon) - 1]
    # Mewtwo
    elif roll == 10:
        presentPokemon = wildPokemon[0]
        
    partyLen = len(fuji.getParty())
    curParty = 0
        
    # Use a Pokemon that still has health
    while fuji.getPartyMember(curParty).getHealth() <= 0:
        curParty += 1
    
    # Battle start messages
    if roll != 10:
        input("You see something barrelling towards you! It's a Pokemon!")

    input("A wild {0} appeared! {1}".format(presentPokemon.getName(), presentPokemon.getIntro()))
    input("You sent out {0}.".format(fuji.getPartyMember(curParty).getName()))
    
    # Handle ditto
    if presentPokemon.getName() == "Ditto":
        presentPokemon.isDitto(fuji.getPartyMember(curParty))
        input("The opposing Ditto's imposter ability activates! It copied your Pokemon!")
    
    while((fuji.getPartyMember(curParty).getHealth() > 0 or curParty == partyLen - 1) and presentPokemon.getHealth() > 0):
        
        if fuji.getPartyMember(curParty).getName() == "Ditto":
            fuji.getPartyMember(curParty).isDitto(presentPokemon)
            input("Ditto's imposter ability activates! It copied the opposing Pokemon!")
        
        oppDamageRoll = randrange(1, 9)
        playerDamageRoll = randrange(1, 9)
        choice = input("Do you want to attack, run, try to catch the Pokemon, or heal? (a/r/c/h) ")
        
        while choice != "a" and choice != "r" and choice != "c" and choice != "h" and choice != "A" and choice != "R" and choice != "C" and choice != "H" :
            choice = input("Well, you have to do something. What will you do? (a/r/c/h) ")
        
        # If the player chooses to attack
        if choice == "a" or choice == "A":
            # Choose turn order based on speed
            if fuji.getPartyMember(curParty).getSpeed() >= presentPokemon.getSpeed():
                presentPokemon.isDamaged(fuji.getPartyMember(curParty).getAttack(), playerDamageRoll)
                input("{0} used {1}! The attack did {2} damage and {3} now has {4} HP.".format(fuji.getPartyMember(curParty).getName(), fuji.getPartyMember(curParty).getAttackName(), (fuji.getPartyMember(curParty).getAttack() + playerDamageRoll), presentPokemon.getName(), presentPokemon.getHealth()))
                
                if presentPokemon.getHealth() <= 0:
                    input("{0} fainted!".format(presentPokemon.getName()))
                
                else:
                    fuji.getPartyMember(curParty).isDamaged(presentPokemon.getAttack(), oppDamageRoll)
                    input("The opposing {0} used {1}! The attack did {2} damage and {3} now has {4} HP.".format(presentPokemon.getName(), presentPokemon.getAttackName(), (presentPokemon.getAttack() + oppDamageRoll), fuji.getPartyMember(curParty).getName(), fuji.getPartyMember(curParty).getHealth()))
                    
                    if fuji.getPartyMember(curParty).getHealth() <= 0 and partyLen - 1 > curParty:
                        handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty + 1), fuji)
                        curParty += 1
                        
                    elif fuji.getPartyMember(curParty).getHealth() <= 0:
                        handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty), fuji)
            else:
                fuji.getPartyMember(curParty).isDamaged(presentPokemon.getAttack(), oppDamageRoll)
                input("The opposing {0} used {1}! The attack did {2} damage and {3} now has {4} HP.".format(presentPokemon.getName(), presentPokemon.getAttackName(), (presentPokemon.getAttack() + playerDamageRoll), fuji.getPartyMember(curParty).getName(), fuji.getPartyMember(curParty).getHealth()))
                    
                if fuji.getPartyMember(curParty).getHealth() <= 0 and partyLen - 1 > curParty:
                    handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty + 1), fuji)
                    curParty += 1
                    
                elif fuji.getPartyMember(curParty).getHealth() <= 0:
                    handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty), fuji)
                
                else:
                    presentPokemon.isDamaged(fuji.getPartyMember(curParty).getAttack(), playerDamageRoll)
                    input("{0} used {1}! The attack did {2} damage and {3} now has {4} HP.".format(fuji.getPartyMember(curParty).getName(), fuji.getPartyMember(curParty).getAttackName(), (fuji.getPartyMember(curParty).getAttack() + oppDamageRoll), presentPokemon.getName(), presentPokemon.getHealth())) 
                    if presentPokemon.getHealth() <= 0:
                        input("{0} fainted!".format(presentPokemon.getName()))
        
        # If player tries to run
        elif choice == "r" or choice == "R":
            # Harder to escape if the Pokemon is faster
            chance = random() - (presentPokemon.getSpeed() / 600)
            
            # Can't escape from Mewtwo
            if chance > .5 and presentPokemon.getName() != "Mewtwo":
                input("You got away!")
                break
            
            else:
                input("You couldn't get away!")
                fuji.getPartyMember(curParty).isDamaged(presentPokemon.getAttack(), oppDamageRoll)
                input("The opposing {0} used {1}! The attack did {2} damage and {3} now has {4} HP.".format(presentPokemon.getName(), presentPokemon.getAttackName(), (presentPokemon.getAttack() + oppDamageRoll), fuji.getPartyMember(curParty).getName(), fuji.getPartyMember(curParty).getHealth()))
                
                if fuji.getPartyMember(curParty).getHealth() <= 0 and partyLen - 1 > curParty:
                    handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty + 1), fuji)
                    curParty += 1
                    
                elif fuji.getPartyMember(curParty).getHealth() <= 0:
                    handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty), fuji)   
        
        # If player tries to catch the Pokemon
        elif choice == "c" or choice == "C":
            
            if fuji.getItem(0) == 0 and fuji.getItem(2) == 0:
                input("You have no Poke Balls! Try one of the other options instead.")
            
            else:
                input("You have {0} Poke Ball(s) and {1} Master Ball(s).".format(fuji.getItem(0), fuji.getItem(2)))
                typeOfBall = input("Do you want to use a Poke Ball or a Master Ball? (p/m) ")
                
                # Catching with a Poke Ball is easier if the opponent has more damage
                if (typeOfBall == "p" or typeOfBall == "P") and fuji.getItem(0) > 0:
                    input("You threw a Poke Ball.")
                    fuji.useItem(0)
                    catchRate = random() + ((1 - (presentPokemon.getHealth() / 250)) / 8)
                    
                    if catchRate > .5:
                        input("You caught it! {0} has been added to your party.".format(presentPokemon.getName()))
                        
                        presentPokemon.restoreStartingHealth()
                        newPartyMem = Pokemon(presentPokemon.getName(), presentPokemon.getAttack(), presentPokemon.getHealth(), presentPokemon.getSpeed(), presentPokemon.getAttackName(), presentPokemon.getIntro())
                        fuji.catchPokemon(newPartyMem)
                        break
                    
                    if catchRate <= .6:
                        input("Shoot, it got out. It was so close, too!")
                        input("Tip: Damaging a Pokemon makes it easier to catch.")
                        fuji.getPartyMember(curParty).isDamaged(presentPokemon.getAttack(), oppDamageRoll)
                        input("The opposing {0} used {1}! The attack did {2} damage and {3} now has {4} HP.".format(presentPokemon.getName(), presentPokemon.getAttackName(), (presentPokemon.getAttack() + oppDamageRoll), fuji.getPartyMember(curParty).getName(), fuji.getPartyMember(curParty).getHealth()))
                
                        if fuji.getPartyMember(curParty).getHealth() <= 0 and partyLen - 1 > curParty:
                            handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty + 1), fuji)
                            curParty += 1
                            
                        elif fuji.getPartyMember(curParty).getHealth() <= 0:
                            handleFainting(partyLen, curParty, fuji.getPartyMember(curParty), fuji.getPartyMember(curParty), fuji)
                
                # Using a Master Ball
                elif (typeOfBall == "m" or typeOfBall == "M") and fuji.getItem(2) > 0:
                    input("You threw a Master Ball.")
                    fuji.useItem(2)
                    input("You caught it! {0} has been added to your party.".format(presentPokemon.getName()))
                    
                    presentPokemon.restoreStartingHealth()
                    newPartyMem = Pokemon(presentPokemon.getName(), presentPokemon.getAttack(), presentPokemon.getHealth(), presentPokemon.getSpeed(), presentPokemon.getAttackName(), presentPokemon.getIntro())
                    fuji.catchPokemon(newPartyMem)
                    break
                
                else:
                    input("You don't have enough of those! Pick another option.")
        
        elif choice == "h" or choice == "H":
            if fuji.getItem(3) == 0:
                input("You have no Super Potions! Try one of the other options instead.")
            
            else:
                fuji.getPartyMember(curParty).restoreStartingHealth()
                fuji.useItem(3)
                input("{0} regained its health! It now has {1} HP.".format(fuji.getPartyMember(curParty).getName(), fuji.getPartyMember(curParty).getHealth()))
    
    # Wild Pokemon shouldn't still be damaged from the previous battle
    presentPokemon.restoreStartingHealth()
    if presentPokemon.getName() != "Mewtwo":
        input("You continue on through the cave.")
    print("")

# When a player's Pokemon faints
def handleFainting(partyLen, curParty, pokemon1, pokemon2, fuji):
        input("{0} fainted!".format(pokemon1.getName()))
        
        if partyLen - 1 > curParty:
            curParty += 1
            input("You sent out {0}.".format(pokemon2.getName()))
        else:
            print("\nYou have no Pokemon left! You use the Escape Rope and leave the cave. Let's hope Team Rocket decides to be forgiving.")
            print("\nGame over!")
            partyStr = "Ending party: "
            for pokemon in fuji.getParty():
                if pokemon.getName() == "Charizard":
                    partyStr = partyStr + pokemon.getName() + " (" + str(pokemon.getHealth()) + " HP)"
                else:
                    partyStr = partyStr + ", " + pokemon.getName() + " (" + str(pokemon.getHealth()) + " HP)"
            print(partyStr)
            print("Ending inventory: {0} Poke Ball(s), {1} Nugget(s), {2} Master Ball(s), {3} Super Potion(s)".format(fuji.getItem(0), fuji.getItem(1), fuji.getItem(2), fuji.getItem(3)))
            quit()

main()        