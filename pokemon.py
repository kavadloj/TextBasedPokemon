# Jonah Kavadlo
class Pokemon:
    def __init__(self, name, attack, health, speed, attackName, intro):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        self.attackName = attackName
        self.intro = intro
        
        self.startingHealth = health
    
    def getName(self):
        return self.name
    
    def getAttackName(self):
        return self.attackName
    
    def getAttack(self):
        return self.attack
    
    def getIntro(self):
        return self.intro
    
    def getHealth(self):
        if self.health < 0:
            return 0
        
        else:
            return self.health
    
    def getSpeed(self):
        return self.speed
    
    def isDamaged(self, opponentAttack, damageRoll):
        self.health = self.health - (opponentAttack + damageRoll)
        
    def restoreStartingHealth(self):
        self.health = self.startingHealth
        
    def isDitto(self, pokemon):
        self.attack = pokemon.getAttack()
        self.attackName = pokemon.getAttackName()
        self.speed = pokemon.getSpeed()