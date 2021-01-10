def zombie_attack(wave, inventory,health):
    '''
    goes through the current wave that the hero must survive
    parameters: wave: int, inventory: dictionary, health: int
    returns: z_list: list
    '''
    zombies = wave * 3
    z_health = wave * 2
    count = 0
    total_damage = 0
    # loop to go through each zombie
    for zombie in range(0, zombies+1, 1):
        # sets the damage per zombie
        damage = wave * 1
        # loop until the zombie is dead
        while z_health >0:
            z_health -= inventory['weapon']
            # amount of attacks it takes to kill the zombie
            count += 1
        # checks how many attacks it took to kill the zombie
        # and determines how many times the hero will get hit
        if count == 1:
            hit = 0
        elif count <=3:
            hit = 1
        elif count <=5:
            hit = 2
        elif count <=7:
            hit = 3
        elif count >=10:
            hit = 4
        # reduces the damage based on armor rating
        if inventory['armor'] <= 4:
            damage -= 1
        elif inventory['armor'] <= 6:
            damage -= 2
        elif inventory['armor'] <= 8:
            damage -= 3
        elif inventory['armor'] >= 10:
            damage -= 4
        # calculates the total damage that the hero will take
        total_damage += (damage*hit)
        health -= (damage*hit)
        max_zom = zombie-1
        # calculates the money the hero earned
    money = zombies* 10
    # list of all the variables found in the function
    z_list=[total_damage, money, max_zom]
    return z_list
