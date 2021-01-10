def buy_armor(inventory,a_def,a_price,a_upgrade):
    '''
    buys the armor that the blacksmith is offering
    parameters: inventory: dictionary, a_def: int, a_price: int, a_upgrade: int
    returns: inventory: dictionary, a_def: int, a_price: int, a_upgrade: int
    '''
    # if the hero can afford the armor and if it was not already bought
    # then the armor will be purchased
    if inventory['Money'] >= a_price and a_def !=0:
        inventory['Money'] = inventory['Money'] - a_price
        inventory['armor'] = a_def
        # sets the price and defense for blacksmith's
        # armor to 0 so it cannot be bought again
        a_def = 0
        a_price = 0
        # sets the armor upgrade to 0, since it is new armor
        a_upgrade = 0
    # the user sees that the hero cannot buy the armor
    else:
        print('You can\'t buy that armor')
    return inventory, a_def,a_price,a_upgrade

def buy_weapon(inventory,w_dam,w_price,w_upgrade):
    '''
    buys the weapon that the blacksmith is offering
    parameters: inventory: dictionary, w_dam: int, w_price: int, w_upgrade: int
    returns: inventory: dictionary, w_dam: int, w_price: int, w_upgrade: int
    '''
    # if the hero can afford the weapon and if it was not already bought
    # then the weapon will be purchased
    if inventory['Money'] >= w_price:
        inventory['Money'] = inventory['Money'] - w_price
        inventory['weapon'] = w_dam
        # sets the price and damage for the blacksmith's
        # weapon to 0 so it cannot be bought again
        w_dam = 0
        w_price = 0
        # sets the weapon upgrade back to zero, since it
        # is a new weapon
        w_upgrade = 0
    # the user sees that the hero cannot buy the weapon
    else:
        print('You can\'t buy that weapon')
    return inventory,w_dam,w_price,w_upgrade

def buy_healing(inventory,quantity,h_price,h_quan):
    '''
    buys healing potions the blacksmith is offering
    parameters: inventory: dictionary, quantity: int, h_price: int, h_quan: int
    returns: inventory: dictionary, quantity: int, h_price: int, h_quan: int
    '''
    # if the hero can afford the healing potions and if the user's quantity
    # is lower than or equal to the blacksmith's, then the healing potions will
    # be purchased
    if inventory['Money'] >= (h_price*quantity) and quantity <= h_quan:
        inventory['Money'] = inventory['Money'] - (quantity*h_price)
        inventory['Healing potions'] += quantity
        h_quan -= quantity
    # displays that the hero has requested too many potions
    elif quantity > h_quan:
        print('You can\'t buy that many potions. The blacksmith only has',\
              h_quan)
    # displays that the hero can't afford the potions
    elif inventory['Money'] < (h_price*quantity):
        print('You can\'t afford that many healing potions')
    return inventory,quantity, h_price, h_quan
