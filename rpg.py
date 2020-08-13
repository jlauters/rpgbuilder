import random
from levels import level_one
from rpg_character import rpgCharacter

hero = rpgCharacter("Bleep", "Orc", "Mage", ["Stamina", "Strength"], 1, 100, 0)

print("Our Hero: ")
hero.status()

currlvl = level_one.levelOne()

print("Level One: ")
currlvl.printMap()

# handle character movement on map
def exploreMap(level):
    
    # Set our start, path, and end points
    curr_pos    = level.start[0]
    opensquares = level.opensquares
    finish      = level.finish[0]

   
    # Make a Move ....
    for(row, square) in enumerate(opensquares):
        # square gives coords as (col, row)

        diceroll = random.randrange(20)
        if(15 >= diceroll):
            print( "enemy encounter" )

            minion = rpgCharacter("Doop", "Goblin", "Minion", ["N/A"], 1, random.randrange(10), 0)


            # Fight enemy until either it dies or hero dies
            while( hero.health > 0 and minion.health > 0):
                hero_attack = hero.attack()
                enemy_attack = minion.attack()

                if(hero_attack):
                    print("hero does " + str(hero_attack) + " damage")
                    minion.damage(hero_attack)
   
                if(enemy_attack):
                    print("enemy does " + str(enemy_attack) + " damage")
                    hero.damage(enemy_attack)
 
            if(minion.health <= 0):
                print("enemy is dead")

                hero.addXp(10)
                if(hero.xp >= 100):
                    hero.levelUp()

                hero.status()



        # Check for Up / Down
        if(square[0] == curr_pos[0] and square[1] == (curr_pos[1] + 1)):
            print("Move Down")
            curr_pos = square

        if(square[0] == curr_pos[0] and square[1] == (curr_pos[1] - 1)):
            print("Move Up")
            curr_pos = square

        # Check for Left / Right
        if(square[0] == (curr_pos[0] + 1) and square[1] == curr_pos[1]):
            print("Move Right")
            curr_pos = square

        if(square[0] == (curr_pos[0] - 1) and square[1] == curr_pos[1]):
            print("Move Left")
            curr_pos = square       

    print('open squares complete ..')

    # After opn squares, check if we're right next to finish
    # Check for Up / Down
    if(finish[0] == curr_pos[0] and finish[1] == (curr_pos[1] + 1)):
        print("Finish Down")
        curr_pos = finish

    if(finish[0] == curr_pos[0] and finish[1] == (curr_pos[1] - 1)):
        print("Finish Up")
        curr_pos = finish

    # Check for Left / Right
    if(finish[0] == (curr_pos[0] + 1) and finish[1] == curr_pos[1]):
        print("Finish Right")
        curr_pos = finish


    if(finish[0] == (curr_pos[0] - 1) and finish[1] == curr_pos[1]):
        print("Finish Left")
        curr_pos = finish


    if(curr_pos == finish):
        print("End Level")


exploreMap(currlvl)



#handle probability of enemey or item encounter
#
# handle combat
