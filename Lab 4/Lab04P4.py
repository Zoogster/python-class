import random

computer_pick = random.randint(6, 9)
for i in range(3):
    player_pick = random.randint(1, 10)
    print('Your pick: ', player_pick)
    if player_pick > computer_pick:
        print('You have won the game!')
        break
else:
    print('Sorry, you have lost the game.')
