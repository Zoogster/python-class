from dinner_combo import Dinner_combo


class Deluxe_dinner_combo(Dinner_combo):

    def __init__(self):
        # call super().__init__()
        super().__init__()
        self._appetizer = ''
        # create self._appetizer and initialize it to empty string

    def choose_appetizer(self):
        # input choice, store appetizer name in self._apprtizer and add appetizer price to self._total
        choice = int(input(
            'Enter 1 for spring roll [$1.25] or 2 for chicken wing [$1.50]: '))
        if choice == 1:
            self._appetizer = 'spring roll'
            self._total = self._total + 1.25
        elif choice == 2:
            self._appetizer = 'chicken wing'
            self._total = self._total + 1.50

    def displayOrder(self):
        # display self._appetizer, self._soup, self._main_dish and self._total
        print(
            f'Items ordered: {self._appetizer}, {self._soup}, {self._main_dish}')
        print(f'Please pay $ {self._total:.2f}')
