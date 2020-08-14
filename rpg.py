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
    # Reverse our start and finish tupels for sanity
    curr_pos    = level.start[0][::-1]
    opensquares = level.opensquares
    finish      = level.finish[0][::-1]


    # Make a Move ....
    for(row, square) in enumerate(opensquares):

        square = square[::-1]

        diceroll = random.randrange(20)
        if(15 >= diceroll):
            print( "enemy encounter" )

            minion = rpgCharacter("Doop", "Goblin", "Minion", ["N/A"], 1, random.randrange(1,10), 0)

            # Fight enemy until either it dies or hero dies
            while( hero.health > 0 and minion.health > 0):
                hero_attack  = hero.attack()
                enemy_attack = minion.attack()

                if(hero_attack):
                    print("hero does " + str(hero_attack) + " damage")
                    minion.damage(hero_attack)
                else:
                    print("hero misses ...")
   
                if(enemy_attack):
                    print("enemy does " + str(enemy_attack) + " damage")
                    hero.damage(enemy_attack)
                else:
                    print("enemy misses ...") 

            if(minion.health <= 0):
                print("enemy is dead - hero earns 10 XP!")
                hero.addXp(10)
                if(hero.xp >= 100):
                    hero.levelUp()

                hero.status()

        # square gives coords as (col, row)
        # Check for Right / Left
        if(square[0] == curr_pos[0] and square[1] == (curr_pos[1] + 1)):
            print("Move Right")

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

            curr_pos = square

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
            level.printMap()

        if(square[0] == curr_pos[0] and square[1] == (curr_pos[1] - 1)):
            print("Move Left")

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

            curr_pos = square

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
            level.printMap()

        # Check for Down / Up
        if(square[0] == (curr_pos[0] + 1) and square[1] == curr_pos[1]):
            print("Move Down")

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

            curr_pos = square

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
            level.printMap()

        if(square[0] == (curr_pos[0] - 1) and square[1] == curr_pos[1]):
            print("Move Up")

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

            curr_pos = square

            level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
            level.printMap()


    # After open squares, check if we're right next to finish
    # Check for Right / Left
    if(finish[0] == curr_pos[0] and finish[1] == (curr_pos[1] + 1)):
        print("Finish Right")

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

        curr_pos = finish

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
        level.printMap()

    if(finish[0] == curr_pos[0] and finish[1] == (curr_pos[1] - 1)):
        print("Finish Left")

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

        curr_pos = finish

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
        level.printMap()

    # Check for Down / Up
    if(finish[0] == (curr_pos[0] + 1) and finish[1] == curr_pos[1]):
        print("Finish Down")

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

        curr_pos = finish

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
        level.printMap()

    if(finish[0] == (curr_pos[0] - 1) and finish[1] == curr_pos[1]):
        print("Finish Up")

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "."

        curr_pos = finish

        level.matrix[ curr_pos[0] ][ curr_pos[1] ] = "C"
        level.printMap()


    if(curr_pos == finish):

        print("\n")
        print("*****************************************************")
        print("**           Level End - Good Job!                 **")
        print("*****************************************************")
        print("\n")

exploreMap(currlvl)



#handle probability of enemey or item encounter
#
# handle combat
