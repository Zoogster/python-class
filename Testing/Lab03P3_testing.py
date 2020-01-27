delivery_type = input(
    'Please enter the type of shipping you would like. For standard please enter put an "S". For express please enter an "E". ')
delivery_type = delivery_type.upper()
weight = float(input('Please enter weight of package in pounds: '))
if delivery_type == 'S':
    if weight > 4 and weight <= 8:
        rate = 1.05
    elif weight > 8 and weight <= 15:
        rate = 0.85
    elif weight > 15:
        rate = 80
if delivery_type == 'E':
    if weight <= 2:
        rate = 3.25
    elif weight > 2 and weight <= 5:
        rate = 2.95
    elif weight > 5 and weight <= 10:
        rate = 2.75
    elif weight > 10:
        rate = 2.55
shipping_charge = rate * weight
print('The shipping charge will be: $', shipping_charge)


# elif delivery_type == 'S' and weight > 4 and weight <= 8:
#     rate = 0.95
# elif delivery_type == 'S' and weight > 8 and weight <= 15:
#     rate = 0.85
# elif delivery_type == 'S' and weight > 15:
#     rate = 0.80
# elif delivery_type == 'E' and weight <= 2:
#     rate = 3.25
# elif delivery_type == 'E' and weight > 2 and weight <= 5:
#     rate = 2.95
# elif delivery_type == 'E' and weight > 5 and weight <= 10:
#     rate = 2.75
# elif delivery_type == 'E' and weight > 10:
#     rate = 2.55
# shipping_charge = rate * weight
# print('The shipping charge will be: $% .2f' % shipping_charge)
