customer_type = input(
    'Enter R for residential customer or B for business customer: ')
gallons_of_water = float(input('How many gallons of water were used? '))
customer_type = customer_type.upper()
if customer_type == 'R':
    low_rate = 0.005
    high_rate = 0.007
    if gallons_of_water <= 6000:
        total_cost = gallons_of_water * low_rate
    else:
        total_cost = (6000 * low_rate) + \
            ((gallons_of_water - 6000) * high_rate)
if customer_type == 'B':
    low_rate = 0.006
    high_rate = 0.008
    if gallons_of_water <= 8000:
        total_cost = gallons_of_water * low_rate
    else:
        total_cost = (8000 * low_rate) + \
            ((gallons_of_water - 8000) * high_rate)
print('The total cost of water is: ', total_cost)
