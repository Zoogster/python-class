while True:
    car_type = input('Enter S for SUV, M for minivan, H for hybrid: ')
    car_type = car_type.upper()
    if car_type == 'S':
        break
    elif car_type == 'M':
        break
    elif car_type == 'H':
        break
    else:
        print('Invalid car type.')

while True:
    amount_of_days = int(input('Enter number of days: '))
    if amount_of_days >= 2:
        break
    else:
        print('Must be at least 2 days.')

if car_type == 'S':
    if amount_of_days <= 7:
        rental_fee = amount_of_days*55
    else:
        rental_fee = 7*55 + (amount_of_days-7)*47
elif car_type == 'M':
    if amount_of_days <= 7:
        rental_fee = amount_of_days*49
    else:
        rental_fee = 7*49 + (amount_of_days-7)*42
elif car_type == 'H':
    if amount_of_days <= 7:
        rental_fee = amount_of_days*44
    else:
        rental_fee = 7*44 + (amount_of_days-7)*38

print('Rental fee: ', rental_fee)
