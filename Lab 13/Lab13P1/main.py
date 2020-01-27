from dinner_combo import Dinner_combo
from deluxe_dinner_combo import Deluxe_dinner_combo


def main():
    # inout meal choice
    choice = int(
        input('Enter 1 for dinner combo or 2 for deluxe dinner combo: '))

    if choice == 1:
        dinner = Dinner_combo()
        dinner.choose_soup()
        dinner.choose_main_dish()
        dinner.displayOrder()

    elif choice == 2:
        # create DeluxeDinnerCombo object and call its methods
        dinner = Deluxe_dinner_combo()
        dinner.choose_appetizer()
        dinner.choose_soup()
        dinner.choose_main_dish()
        dinner.displayOrder()


main()
