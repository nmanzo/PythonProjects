#-------------------------------------------------------------------------------
# Student Name: Nathan Manzo
# Python version: 3.6.4
# Submission Date: 12/01/2018
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
# Pseudocode:
# 1) make a while loop to ask the user if they want to play again after they die
# 2) present an intro, ask the user for the hero's name, and set the hero's
# inventory with a dictionary
# 3) intialize health, upgrade, wave and zobmies killed variables
# 4) start loop to repeat the same pattern for each wave, like choices
# 5) run zombie attack function to get the hero's total damage they recieved,
# the money they got for the wave, and the zombies the hero killed
# 6) tell the user if they survived the wave, if they did not survive then 
# a message will display the total zombies they killed before they died
# 7) if the hero survived then the user will be asked what they want to do
# before the next wave arrives
# 8) They will have five options: 1) buy new stuff from the blacksmith, 2)
# upgrade their current equipment, 3) use a healing potion, 4) search the
# field for better supplies, or 5) escape the zombies
# 9) after the user has picked their option, the next wave begins
# 10) this continues until the hero's health falls to 0 or if the user picks 
# option 5, then are asked if they want to play it again
import zombie
import buy
import action



def main():
    replay = 1
    # intro into the world for the first time they play
    print('A hero is one of the last humans in a zombie apocalypse.')
    print('They hear a large horde of zombies coming their way.')
    print('The hero takes their worn out armor and rusty weapon to prepare for the')
    print("first of "\
          'many waves of zombies that will be attempting to kill our hero \n')
    print('As their on their way out to fight off the zombies, they pass by the')
    print('blacksmith. The hero checks to see if he has you want to'
          'upgrade your armor')
    print('or weapon, then the realizes they don\'t have enough money, and face')
    print('the horde.')
    while replay == 1:
        difficulty = input('What difficulty would you like to play on'\
                           '(e for easy, m for medium, or h for hard)?\n')
        difficulty = difficulty.lower()
        # inital inventory for the hero based on difficulty
        if difficulty == 'e':
            inventory = {'weapon':8, 'armor': 8, 'Money': 150,
                         'Healing potions': 7}
            # hero's starting health
            health = 30
        elif difficulty == 'm':
            inventory = {'weapon':5, 'armor': 5, 'Money': 100,
                         'Healing potions': 5}
            # hero's starting health
            health = 20
        elif difficulty == 'h':
            inventory = {'weapon':3, 'armor': 3, 'Money': 50,
                         'Healing potions': 3}
            # hero's starting health
            health = 10
        else:
            print('invalid choice, game mode will be set to hard')
            difficulty = 'h'
            inventory = {'weapon':3, 'armor': 3, 'Money': 50,
                         'Healing potions': 3}
            # hero's starting health
            health = 10
        # user gets to assign a name to the hero
        name = input('What is the hero\'s name?\n')
        
        # intital wave
        wave = 1
        # tracks the total zombies the hero killed
        zomb = 0
        # intial value for the weapon upgrade
        w_upgrade = 0
        # intial value for the armor upgrade
        a_upgrade = 0
    
        # loop until the hero's health is below 0
        while health > 0:
            # gets the total damage the hero suffered, money obtained for the wave,
            # and the zombies slain
            stuff = zombie.zombie_attack(wave, inventory, health)
            # damages the hero
            health = health - stuff[0]
            # total zombies defeated
            zomb += stuff[2]
            # adds the money from the round to the hero's inventory
            inventory['Money']+=stuff[1]
            # if the hero is not dead, these options will be available
            if health > 0:
                # says which wave was just completed and gives the user options
                # for what they want to do next
                print(name, 'Has defeated wave',wave,'of the zombies\n')
                print('What does',name,'want to do before the next wave?')
                print('1) buy new gear or healing potions from the blacksmith')
                print('2) upgrade your current gear at the blacksmith')
                print('3) use a healing potion (heals 10 health)')
                print('4) search the field for maybe something good')
                print('5) try to escape the horde\n')
                # displays the hero's inventory to the user
                print('The hero has ',inventory['Money'],' dollars')
                print('The hero\'s weapon does',inventory['weapon'],'damage')
                print('The hero\'s armor has a defense of',inventory['armor'])
                print('The hero has',inventory['Healing potions'],'healing potions')
                print(name,'has',health,'health')
                choice = int(input('Which option do you pick?\n'))
                # if choice is 1, then go to blacksmith to buy gear
                if choice == 1:
                    # inital values for gear sold by blacksmith
                    choice2 = 1
                    # weapon damage that blacksmith's weapon does
                    w_dam = wave*3
                    # price for the blacksmith's weapon
                    w_price = wave*50
                    # defense of the armor that the blacksmith is selling
                    a_def = wave*2
                    # price the armor is being sold for
                    a_price = wave*60
                    # price for healing potions
                    h_price = 50
                    # the amount of healing potions the blacksmith has
                    h_quan = 3
                    #loop until choice2 is less than 0 or greater than 4
                    while 0 < choice2 < 4:
                        # print menu for the user
                        print('Blacksmith')
                        print('1) weapon \tdamage:',w_dam,'\tprice:',w_price)
                        print('2) armor \tdefense:',a_def,'\tprice:',a_price)
                        print('3) healing potions \tquantity: ',h_quan,\
                              '\tprice for one:',h_price)
                        print('4) exit store\n')
                        print(name+'\'s money',inventory['Money'],'\n')
                        # asks the user what option they want to pick
                        choice2 = int(input('Which do you want to do?\n'))
                        # checks which option the user picked
                        if choice2 ==1:
                            # buys the weapon and replaces the old one's damage
                            # with the new one's damage and resets the upgrade
                            # to 0
                            inventory,w_dam,w_price,w_upgrade = \
                            buy.buy_weapon(inventory,w_dam,w_price, w_upgrade)
                            print('\nYour weapon now deals',inventory['weapon']\
                              ,'and you now have', inventory['Money'],'dollars')
                        elif choice2 ==2:
                            # buys the armor and replaces the old one's defense
                            # with the new one's defense and resets the upgrade
                            # to 0
                            inventory,a_def,a_price,a_upgrade = \
                            buy.buy_armor(inventory,a_def,a_price,a_upgrade)
                            print('\nYour armor has a defense of'\
                                  ,inventory['armor'],\
                              'and you now have', inventory['Money'],'dollars')
                        elif choice2 ==3:
                            # asks the user how many healing potions they want
                            # to buy
                            quantity = int(input('How many do you want to buy?'\
                                                 '\n'))
                            # calls the buy healing function to purchase the
                            # healing potions
                            inventory,quantity,h_price,h_quan = \
                            buy.buy_healing(inventory,quantity,h_price,h_quan)
                            print('\nYou now have',inventory['Healing potions']\
                                  ,'healing potions and', inventory['Money'],\
                                  'dollars')
                        # tells the user that they have left the store
                        else:
                            print('You leave the store to go back into battle')
                elif choice == 2:
                    # intializes choice 3 variable
                    choice3 = 1
                    # loop to check if the user picked an option that
                    # is acceptable
                    while 0 < choice3 < 3:
                        # sets the price for weapon and armor upgrades
                        if w_upgrade == 0:
                            w_up_price = 50
                        elif w_upgrade > 0:
                            w_up_price = (w_upgrade+1)*50
                        if a_upgrade == 0:
                            a_up_price = 50
                        else:
                            a_up_price = (a_upgrade+1)*50
                        # prints what the choices are for upgrades
                        print('Blacksmith upgrades')
                        print('1) weapon upgrade price:',w_up_price)
                        print('2) armor upgrade price:',a_up_price)
                        print('3) exit store\n')
                        print(name+'\'s money',inventory['Money'],'\n')
                        print('The hero\'s weapon does',inventory['weapon'],\
                              'damage')
                        print('The hero\'s armor has a defense of',\
                              inventory['armor'])
                        # asks the user what choice they want to make
                        choice3 = int(input('What do you want to do?\n'))
                        if choice3 == 1:
                            # upgrades the weapon damage
                            inventory,w_upgrade = \
                            action.upgrade_weapon(inventory,w_upgrade,\
                                                  w_up_price)
                        elif choice3 == 2:
                            # upgrades the armor defense
                            inventory,a_upgrade = \
                            action.upgrade_armor(inventory,a_upgrade,a_up_price)
                        else:
                            print('You leave the store to go back into battle')
                # if the choice is 3 then a healing potion will be used
                elif choice == 3:
                    # heals the hero and takes away one healing potion away
                    # from their inventory
                    inventory, health = action.use_healing(inventory,health,\
                                                           difficulty)
                # choice 4 searches the battlefield for possible equipment
                # for the hero to use
                elif choice == 4:
                    inventory = action.search(inventory, wave)
                # choice 5 ends the program
                elif choice == 5:
                    print(name,'tried to escape, but there were too many')
                    print(name,'has been killed by the zombies')
                    print(name,'killed',zomb,'zombies')
                    break
                else:
                    print('invalid choice, starting next wave')
                wave+=1
            else:
            # the hero's total zombies killed is displayed and lets the user
            # know that they have lost
                print(name,'has been killed by the zombies')
                print(name,'killed',zomb,'zombies')
        # asks the user if they would like to replay the game
        replay = int(input('Do you want to play again 1) yes or 2) no\n'))

main()
