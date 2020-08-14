import random
from levels import level_one, level_two
from rpg_character import rpgCharacter

# Gotta have a banner right?
print("__________  __________   ________  __________        .__ .__       .___               ") 
print("\______   \ \______   \ /  _____/  \______   \ __ __ |__||  |    __| _/  ____  _______") 
print(" |       _/  |     ___//   \  ___   |    |  _/|  |  \|  ||  |   / __ | _/ __ \ \_  __ \\")
print(" |    |   \  |    |    \    \_\  \  |    |   \|  |  /|  ||  |__/ /_/ | \  ___/  |  | \/")
print(" |____|_  /  |____|     \______  /  |______  /|____/ |__||____/\____ |  \___  > |__|   ")
print("        \/                     \/          \/                       \/      \/         ")


hero = rpgCharacter("Bleep", "Orc", "Mage", ["Stamina", "Strength"], 1, 100, 0)
hero.status()

print("Level One: ")
currlvl = level_one.levelOne()
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

        # reverse our open square tupel for sanity
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


# Run the thing ..
exploreMap(currlvl)

# Next Level
currlvl = level_two.levelTwo()
exploreMap(currlvl)

