def main():
    kWh_used = float(input('Enter Kilowatt hours used: '))
    customer_type = input(
        'Enter R for residential customer, B for business customer: ')
    customer_type = customer_type.upper()
    bill_calculator(kwhu=kWh_used, ct=customer_type)


def bill_calculator(kwhu, ct):
    if ct == 'R':
        if kwhu > 500:
            bill = (0.12 * 500) + 0.15 * (kwhu - 500)
        else:
            bill = 0.12 * kwhu
    else:
        if kwhu > 800:
            bill = (0.16 * 800) + 0.20 * (kwhu - 800)
        else:
            bill = 0.16 * kwhu
    print(f'Please pay this amount: {bill: .2f}')


main()
