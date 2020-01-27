def main():
    kWh_used = float(input('Enter Kilowatt hours used: '))
    bill_calculator(kWh_used)


def bill_calculator(kWh_used):
    if kWh_used > 500:
        bill = (0.12 * 500) + 0.15 * (kWh_used - 500)
    else:
        bill = 0.12 * kWh_used
    print(f'Please pay this amount: {bill: .2f}')


main()
