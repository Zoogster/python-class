hotdogs_bought = float(input('Enter number of hotdogs being bought: '))
chip_bags_bought = float(input('Enter number of chip bags being bought: '))
soda_cans_bought = float(input('Enter number of soda cans being bought: '))
hotdog_cost = hotdogs_bought * 2.50
chip_cost = chip_bags_bought * 1.50
soda_cost = soda_cans_bought * 1.25
total_amount_due = hotdog_cost + chip_cost + soda_cost
print('Total due: $', total_amount_due)
