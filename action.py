def upgrade_weapon(inventory,w_upgrade,w_up_price):
    '''
    upgrades the weapon damage by 1
    parameters: inventory: dictionary, w_upgrade: int, w_price: int
    return: inventory: dictionary, w_upgrade: int
    '''
    # checks if the hero has enough money to afford an upgrade
    if inventory['Money'] < w_up_price:
        print('You don\'t have enough money to upgrade that')
    # if hero has enough money then the weapon will be upgraded by 1
    else:
        # keeps track of how many times the weapon is upgraded
        w_upgrade += 1
        # takes money away from the hero to pay for the upgrade
        inventory['Money'] -= w_up_price
        # the weapon damage is increased by 1
        inventory['weapon'] += 1
        # raises the price of the weapon upgrade
        w_up_price = w_upgrade*50
    return inventory, w_upgrade
        
def upgrade_armor(inventory,a_upgrade,a_up_price):
    '''
    upgrades the armor defense by 1
    parameters: inventory: dictionary, a_upgrade: int, a_price: int
    return: inventory: dictionary, a_upgrade: int
    '''
    # checks if the hero has enough money to afford an upgrade
    if inventory['Money'] < a_up_price:
        print('You don\'t have enough money to upgrade that')
    # if hero has enough money then the armor will be upgraded by 1
    else:
        # keeps track of how many times the armor is upgraded
        a_upgrade += 1
        # takes money away from the hero to pay for the upgrade
        inventory['Money'] -= a_up_price
        # the armor defense is increased by 1
        inventory['armor'] += 1
        # raises the price of the armor upgrade
        a_up_price = a_upgrade*50
    return inventory, a_upgrade

def use_healing(inventory,health,difficulty):
    '''
    heals the hero back to full health
    parameters: inventory: dictionary, health: int, difficulty: string
    return: inventory: dictionary, health
    '''
    # checks the users health and difficulty to heal the hero to the
    # appropiate health
    # hard difficulty option
    if health == 10 and difficulty == 'h':
        print('You are already at full health')
    elif health != 10 and difficulty =='h':
        inventory['Healing potions'] -= 1
        health = 10
        print('You are now at full health')
    # medium difficulty option
    if health == 20 and difficulty == 'm':
        print('You are already at full health')
    elif health != 20 and difficulty =='m':
        inventory['Healing potions'] -= 1
        health = 20
        print('You are now at full health')
    # easy difficulty option
    if health == 30 and difficulty == 'e':
        print('You are already at full health')
    elif health != 30 and difficulty =='e':
        inventory['Healing potions'] -= 1
        health = 30
        print('You are now at full health')
    return inventory, health
    
def search(inventory, wave):
    '''
    uses a random number generator to find loot on the field
    parameters: inventory: dictionary,wave: int
    return: inventory: dictionary
    '''
    import random
    # creates a random integer number generator from 1-100
    search = random.randint(1,100)
    # multiple if statements to determine what the hero will find
    # based on the search variable
    if 0 < search <= 25:
        inventory['Healing potions'] += 1
        print('You found 1 healing potion\nHealing potions:'\
              , inventory['Healing potions'])
    elif 26 <= search <= 50:
        print('You look around, but weren\'table to find anything')
    elif 51 <= search <= 60:
        inventory['armor'] += wave
        print('You found some slightly better armor\tdefenese:'\
              ,inventory['armor'])
    elif 61 <= search <= 70:
        inventory['weapon'] += wave
        print('You found a slightly better weapon\tdamage:'\
              ,inventory['weapon'])
    elif 71 <= search <= 80:
        inventory['Money'] += (20*wave)
        print('You found ',20*wave,' dollars\nHero\'s money:'\
              , inventory['Money'])
    elif 81 <= search <= 84:
        inventory['Money'] += (30*wave)
        print('You found ',30*wave,' dollars\nHero\'s money:'\
              , inventory['Money'])
    elif 85 <= search <= 88:
        inventory['weapon'] += (2*wave)
        print('You found a better weapon\tdamage:'\
              ,inventory['weapon'])
    elif 89 <= search <= 92:
        inventory['armor'] += (2*wave)
        print('You found better armor\tdefenese:'\
              ,inventory['armor'])
    elif 93 < search <= 96:
        inventory['Healing potions'] += 2
        print('You found 2 healing potions\nHealing potions:'\
              , inventory['Healing potions'])
    elif search == 97:
        inventory['Healing potions'] += 3
        print('You found 3 healing potions\nHealing potions:'\
              , inventory['Healing potions'])
    elif search == 98:
        inventory['Money'] += (50*wave)
        print('You found',50*wave,'dollars\nHero\'s money:'\
              , inventory['Money'])
    elif search == 99:
        inventory['weapon'] += (3*wave)
        print('You found a significantly better weapon\tdamage:'\
              ,inventory['weapon'])
    elif search == 100:
        inventory['armor'] += (3*wave)
        print('You found significantly better armor\tdefenese:'\
              ,inventory['armor'])
    return inventory
