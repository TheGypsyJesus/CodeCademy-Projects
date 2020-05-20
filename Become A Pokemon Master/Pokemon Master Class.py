#Prerequisites---
pokemon_type = {
"Electric":{
"Strong Against":{"Pokemon_Type":["Normal", "Flying", "Grass", "Water"], "Damage_To":2},
"Weak Against":{"Pokemon_Type":["Ground", "Grass", "Electic", "Dragon"], "Damage_To":0.5},
"Resistant To":{"Pokemon_Type":["Flying", "Electric", "Steel"], "Damage_From":0.5},
"Vulnerable To":{"Pokemon_Type":["Ground"],"Damage_From":2}
},
"Fire":{
"Strong Against":{"Pokemon_Type":["Bug", "Steel", "Grass", "Ice"], "Damage_To":2},
"Weak Against":{"Pokemon_Type":["Rock", "Fire", "Water", "Dragon"], "Damage_To":0.5},
"Resistant To":{"Pokemon_Type":["Bug", "Steel", "Fire", "Grass", "Ice"], "Damage_From":0.5},
"Vulnerable To":{"Pokemon_Type":["Ground", "Rock", "Water"],"Damage_From":2}
},
"Water":{
"Strong Against":{"Pokemon_Type":["Ground", "Rock", "Fire"], "Damage_To":2},
"Weak Against":{"Pokemon_Type":["Water", "Grass", "Dragon"], "Damage_To":0.5},
"Resistant To":{"Pokemon_Type":["Steel", "Fire", "Water", "Ice"], "Damage_From":0.5},
"Vulnerable To":{"Pokemon_Type":["Grass", "Electric"], "Damage_From":2}
} ,
"Grass":{
"Strong Against":{"Pokemon_Type":["Ground", "Rock", "Water"], "Damage_To":2},
"Weak Against":{"Pokemon_Type":["Flying", "Poison", "Bug", "Steel", "Fire", "Grass", "Dragon"], "Damage_To":0.5},
"Resistant To":{"Pokemon_Type":["Ground", "Water", "Grass", "Electric"],"Damage_From":0.5},
"Vulnerable To":{"Pokemon_Type":["Flying", "Poison", "Bug", "Fire", "Ice"],"Damage_From":2}
}
}






#Start of Pokemon Class---
class Pokemon:

#Initialize Pokemon---
    def __init__(self, name, level, p_type):
        self.name = name
        self.level = level #Power
        self.p_type = p_type
        self.health = level * 100
        self.max_health = level * 100
        self.is_knocked_out = False

#Create a string to represent actions---
    def __repr__(self):
        if not self.is_knocked_out:
            return "Pokemon: {name}, Level: {level}, Type: {p_type}, Health: {health} is ready for action.".format(name = self.name, level = self.level, p_type = self.p_type, health = self.health)
        return "Pokemon: {name} is currently knocked out!".format(name = self.name)

#Method for knocking out---
    def knocked_out (self):
        self.is_knocked_out = True
        print ("{name} has been knocked out! Oh no!".format(name = self.name))
        self.health = 0

#Method for taking away health---
    def lose_health(self, hp_lost):
        self.health -= hp_lost
        if self.health <= 0:
            self.knocked_out()
        print ("{name} has been hit, their health is now {health}.".format(name = self.name, health = self.health))

#Method for gaining health---
    def gain_health(self, hp_gain):
        self.health += hp_gain
        if self.health <= self.max_health:
            print ("{name} has regained {hp_gain} health!".format(name = self.name, hp_gain = hp_gain))
        else:
            self.health = self.max_health
            print ("{name} has now reached maximum health: {max_health}.".format(name = self.name, max_health = self.max_health))

#Method for revival---
    def revive_poke (self):
        self.is_knocked_out = False
        self.health = 30
        print ("{name} has been revived! {name}\'s current health is {health}.".format(name = self.name, health = self.health))


#Method for attacking (advantage)---
    def power_attack (self, opponent):
        my_type = pokemon_type [self.p_type]
        if opponent.p_type in my_type["Strong Against"]["Pokemon_Type"]:
          print ("Strong Against {name}".format(name=opponent.p_type))
          return my_type["Strong Against"]["Damage_To"]
        elif opponent.p_type in my_type["Weak Against"]["Pokemon_Type"]:
          print ("Weak Against {name}".format(name=opponent.p_type))
          return my_type["Weak Against"]["Damage_To"]
        else:
          return 0

#Method for getting attacked (disadvantage)---
    def power_attack_received (self, opponent):
        my_type = pokemon_type [self.ptype]
        if opponent.p_type in my_type["Resistant To"]["Pokemon_Type"]:
          print ("Resistant To {name}".format(name=opponent.p_type))
          return my_type["Resistant To"]["Damage_From"]
        elif opponent.p_type in my_type["Vulnerable To"]["Pokemon_Type"]:
          print ("Vulnerable To {name}".format(name=opponent.p_type))
          return my_type["Vulnerable To"]["Damage_From"]
        else:
          return 0

#Method for standard attack---
    def attack (self, opponent):
        if not self.is_knocked_out:
          damage = self.power_attack(opponent) * self.level
          print ("Attacking {opponent} with a damage hit of {damage}".format(opponent = opponent.name, damage = damage))
          opponent.lose_health(damage)
        else:
          print ("{name} cannot attack as it's Knocked Down!".format(name=self.name))

#Setting up Pokemons---
class Pikachu(Pokemon):
    def __init__(self, level):
        super().__init__("Pikachu", level, "Electric")

class Charmander(Pokemon):
    def __init__(self, level):
        super().__init__("Charmander", level, "Fire")

class Squirtle(Pokemon):
    def __init__(self, level):
        super().__init__("Squirtle", level, "Water")

class Bulbasaur(Pokemon):
    def __init__(self, level):
        super().__init__("Bulbasaur", level, "Grass")



#Start of Trainer Class---
class Trainer:

#Initialize---
        def __init__(self, name, pokemons, potions):
            self.name = name
            self.pokemon_owned = pokemons
            self.potions = potions
            self.active_pokemon = 0

#Create a string to represent actions---
        def __repr__(self):
            print ("Trainer: {name}".format(name = self.name))
            print ("Pokemon List:")
            for pokemon in self.pokemon_owned:
              print (pokemon)
              print ("Number of available Potions: {potions}".format(potions = self.potions))
              return "Active Pokemon: {name}".format(name = self.pokemon_owned[self.active_pokemon].name)

#Method for giving Potions---
        def give_potion (self):
            if self.potions > 0:
                self.potions -= 1
                if not self.pokemon_owned[self.active_pokemon].is_knocked_out:
                    print("Healing Pokemon {name}".format(name = self.pokemon_owned[self.active_pokemon].name))
                    self.pokemon_owned[self.active_pokemon].gain_health(30)
                else:
                    print("Potion given to {name} will revive them.".format(name = self.pokemon_owned[self.active_pokemon].name))
                    self.pokemon_owned[self.active_pokemon].revive_poke()
            else:
                print("You have no potions left!")

    #Method for attacking trainer---
        def attack_tr (self, trainer):
            print("Attacking trainer {name}".format(name = trainer.name))
            self.pokemon_owned[self.active_pokemon].attack(trainer.pokemon_owned[trainer.active_pokemon])

    #Method for Switching Pokemon---
        def switch_poke (self, new_poke):
            if new_poke >= 0 and new_poke < len(self.pokemon_owned):
                if new_poke == self.active_pokemon:
                    print("You already have this Pokemon active, pick another")
                elif not self.pokemon_owned[new_poke].is_knocked_out:
                    self.active_pokemon = new_poke
                    print("Switching to {name}".format(name = self.pokemon_owned[new_poke].name))
                else:
                    print("{name} is knocked out man, c'mon.".format(name = self.pokemon_owned[new_poke].name))
            else:
                print("You have no Pokemon avialable!")
























# Creating Pokemons
pk1 = Pikachu (8)
pk2 = Pikachu (10)
pk3 = Charmander (3)
pk4 = Charmander (7)
pk5 = Squirtle (4)
pk6 = Squirtle (9)
pk7 = Bulbasaur (5)
pk8 = Bulbasaur (7)

# Creating Trainers
tr1 = Trainer ("Poke", [pk1, pk4, pk6], 6)
tr2 = Trainer ("Mon", [pk2, pk3, pk5], 6)

# tests
tr2.switch_poke(2)

print (tr1)
print (tr2)

pk5.health = 6
tr1.attack_tr(tr2)
tr2.attack_tr(tr1)
tr2.give_potion ()
# tr2.switch_pokemon(0)
tr2.attack_tr(tr1)
