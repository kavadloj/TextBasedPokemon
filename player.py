# Jonah Kavadlo
from pokemon import Pokemon

class Player:
    def __init__(self, name, party, inventory):
        self.name = name
        self.party = party
        self.inventory = inventory
        
    def getParty(self):
        return self.party
    
    def getPartyMember(self, partyIndex):
        return self.party[partyIndex]
    
    def getInventory(self):
        return self.inventory
    
    def getItem(self, itemIndex):
        return self.inventory[itemIndex]
    
    def addItem(self, itemIndex):
        # 0 is Poke Ball, 1 is Nugget, 2 is Master Ball
        self.inventory[itemIndex] = self.inventory[itemIndex] + 1
    
    def useItem(self, itemIndex):
        self.inventory[itemIndex] = self.inventory[itemIndex] - 1
        
    def catchPokemon(self, pokemon):
        self.party.append(pokemon)
