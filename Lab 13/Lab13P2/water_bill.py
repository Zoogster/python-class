from utility_bill import Utility_bill


class Water_bill(Utility_bill):

    def __init__(self, name, address):
        super().__init__(name, address)
        self._gallons_used = 0

    def calculate_charge(self):
        self._gallons_used = float(
            input('How many gallons of water were used: '))
        if self._gallons_used > 6000:
            self._charge = 6000 * 0.005 + (self._gallons_used - 6000) * 0.007
        else:
            self._charge = self._gallons_used * 0.005

    def display_bill(self):
        print('Water Bill')
        print('Name: ', self._name)
        print('Address: ', self._address)
        print('Gallons used: ', self._gallons_used)
        print(f'Please pay ${self._charge}')
