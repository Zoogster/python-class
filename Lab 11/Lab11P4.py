while True:
    hotdogs_bought = input('Enter number of hotdogs being bought: ')
    try:
        hotdogs_bought = int(hotdogs_bought)
    except(ValueError):
        print('Invalid input')
    else:
        if hotdogs_bought < 0:
            print('Invalid input')
        else:
            break
while True:
    chip_bags_bought = input('Enter number of chip bags being bought: ')
    try:
        chip_bags_bought = int(chip_bags_bought)
    except(ValueError):
        print('Invalid input')
    else:
        if chip_bags_bought < 0:
            print('Invalid input')
        else:
            break

while True:
    soda_cans_bought = input('Enter number of soda cans being bought: ')
    try:
        soda_cans_bought = int(soda_cans_bought)
    except(ValueError):
        print('Invalid input')
    else:
        if soda_cans_bought < 0:
            print('Invalid input')
        else:
            break

hotdog_cost = hotdogs_bought * 2.50
chip_cost = chip_bags_bought * 1.50
soda_cost = soda_cans_bought * 1.25
total_amount_due = hotdog_cost + chip_cost + soda_cost

print('Total due: $', total_amount_due)
