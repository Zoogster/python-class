def main():
    kWh_used_return = get_kWh_used()
    bill = bill_calculator(kWh_used_return)
    print(f'Please pay this amount: ${bill: .2f}')


def get_kWh_used():
    while True:
        kWh_used = float(input('Enter kilowatt hours used: '))
        if kWh_used < 0:
            print('Kwh cannot be negative.')
        else:
            break

    return kWh_used


def bill_calculator(kWh_used):
    if kWh_used > 500:
        bill = (0.12 * 500) + 0.15 * (kWh_used - 500)
    else:
        bill = 0.12 * kWh_used
    return bill


main()
