from drone import Drone


def main():
    drone1 = Drone()
    choice = -1
    while choice != 0:
        choice = int(input(
            'Enter 1 for accelerate, 2 for decelerate,3 for ascend, 4 for decend, 0 for exit: '))

        if choice == 1:
            drone1.accelerate()
        elif choice == 2:
            drone1.decelerate()
        elif choice == 3:
            drone1.ascend()
        elif choice == 4:
            drone1.descend()

        print(f'Speed: {drone1.speed} Height {drone1.height}')


main()
