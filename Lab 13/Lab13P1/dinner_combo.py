class Dinner_combo:

    def __init__(self):
        # create self._soup, self._main_dish, initialize then to empty strings
        self._soup = ''
        self._main_dish = ''
        self._total = 0
        # create self._total, initialize it to 0

    def choose_soup(self):
        # input choice, store soup name in self._soup and add soup price to self._total
        choice = int(input(
            'Enter 1 for egg drop soup [$1.25] or 2 for wanton soup [$1.50]: '))
        if choice == 1:
            self._soup = 'egg drop soup'
            self._total = self._total + 1.25
        elif choice == 2:
            self._soup = 'wanton soup'
            self._total = self._total + 1.50

    def choose_main_dish(self):
        # input choice, store main dish name in self._main_dish and add main dish price to self._total
        choice = int(input(
            'Enter 1 for sweet and sour pork [$7], 2 for sesame chicken [$8] or 3 for shrimp fired rice [$9]: '))
        if choice == 1:
            self._main_dish = 'sweet and sour pork'
            self._total = self._total + 7
        elif choice == 2:
            self._main_dish = 'sesame chicken'
            self._total = self._total + 8
        elif choice == 3:
            self._main_dish = 'shrimp fried rice'
            self._total = self._total + 9

    def displayOrder(self):
        # display self._soup, self._main_dish and self._total
        print(f'Items ordered: {self._soup}, {self._main_dish}')
        print(f'Please pay $ {self._total:.2f}')
