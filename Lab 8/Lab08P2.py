def main():
    kWh_used, customer_type = get_user_input()
    bill = bill_calculator(kWh_used, customer_type)
    print(f'Please pay this amount: ${bill: .2f}')


def get_user_input():
    while True:
        kWh_used = float(input('Enter kilowatt hours used: '))
        if kWh_used < 0:
            print('Kwh cannot be negative.')
        else:
            break

    while True:
        customer_type = input(
            'Enter R for residential customer, B for business customer: ')
        customer_type = customer_type.upper()
        if customer_type == 'R' or customer_type == 'B':
            break
        else:
            print('Invalid customer type.')

    return kWh_used, customer_type


def bill_calculator(kWh_used, customer_type):
    if customer_type == 'R':
        if kWh_used > 500:
            bill = (0.12 * 500) + 0.15 * (kWh_used - 500)
        else:
            bill = 0.12 * kWh_used
    else:
        if kWh_used > 800:
            bill = (0.16 * 800) + 0.20 * (kWh_used - 800)
        else:
            bill = 0.16 * kWh_used

    return bill


main()
