from utility_bill import Utility_bill


class Electricity_bill(Utility_bill):

    def __init__(self, name, address):
        super().__init__(name, address)
        self._kwh_used = 0

    def calculate_charge(self):
        self._kwh_used = float(input('How many kilowatt hours used: '))
        if self._kwh_used > 500:
            self._charge = 500 * 0.12 + (self._kwh_used - 500) * 0.15
        else:
            self._charge = self._kwh_used * 0.12

    def display_bill(self):
        print('Electricity Bill')
        print('Name: ', self._name)
        print('Address: ', self._address)
        print('Kilowatt Hours used: ', self._kwh_used)
        print(f'Please pay ${self._charge}')
