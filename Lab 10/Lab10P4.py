# Sorry for the roundabout way of doing this. I wanted to play with fuctions more


def main():
    accounts_import = water_import()

    account_1 = accounts_import[0]
    account_2 = accounts_import[1]
    account_3 = accounts_import[2]
    account_4 = accounts_import[3]

    account_1, account_2, account_3, account_4 = spliter(
        account_1, account_2, account_3, account_4)

    accounts_list = [account_1, account_2, account_3, account_4]
    charge_list = charge_calculator(accounts_list)

    print(
        f'Account number: {accounts_list[0][0]} water charge: {charge_list[0]}')
    print(
        f'Account number: {accounts_list[1][0]} water charge: {charge_list[1]}')
    print(
        f'Account number: {accounts_list[2][0]} water charge: {charge_list[2]}')
    print(
        f'Account number: {accounts_list[3][0]} water charge: {charge_list[3]}')


def water_import():
    input_file = open('water.text', 'r')
    accounts_import = []
    for line in input_file:
        line = line.strip('\n')
        accounts_import.append(line)
    return accounts_import


def spliter(account_1, account_2, account_3, account_4):
    account_1 = account_1.split()
    account_2 = account_2.split()
    account_3 = account_3.split()
    account_4 = account_4.split()
    return account_1, account_2, account_3, account_4


def charge_calculator(accounts_list):
    charge_list = []
    for account in accounts_list:
        if account[1] == 'R':
            if float(account[2]) > 6000:
                charge = 6000 * 0.005 + (float(account[2]) - 6000) * 0.007
            else:
                charge = float(account[2]) * 0.005
        else:
            if float(account[2]) > 8000:
                charge = 8000 * 0.006 + (float(account[2]) - 8000) * 0.008
            else:
                charge = float(account[2]) * 0.006

        charge_list.append(charge)
    return charge_list


main()
