import currency


def main():
    while True:
        currency_type = int(
            input("Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: "))
        if currency_type < 1 or currency_type > 3:
            print("Error: Invalid Choice")
        else:
            break

    while True:
        dollar = float(input("Enter US Dollar amount: "))
        if dollar < 0:
            print("Error: US Dollar cannot be negative.")
        else:
            break

    if currency_type == 1:
        converted_currency = currency.to_euro(dollar)
        print(f"It is converted to , {converted_currency} Euro")
    elif currency_type == 2:
        converted_currency = currency.to_yen(dollar)
        print(f"It is converted to , {converted_currency} Yen")
    else:
        converted_currency = currency.to_peso(dollar)
        print(f"It is converted to , {converted_currency} Peso")


main()
