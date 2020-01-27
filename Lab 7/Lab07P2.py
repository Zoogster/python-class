def main():
    kWh_used = float(input('Enter Kilowatt hours used: '))
    customer_type = input(
        'Enter R for residential customer, B for business customer: ')
    customer_type = customer_type.upper()
    bill_calculator(kWh_used, customer_type)


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
    print(f'Please pay this amount: {bill: .2f}')


main()
