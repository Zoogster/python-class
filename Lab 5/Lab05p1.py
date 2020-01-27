user_num_list = []
while True:
    new_interger = int(input('Enter an integer from 1 to 10: '))
    user_num_list.append(new_interger)
    another = input('Enter another interger [y/n]? ')
    another = another.lower()
    if another != 'y':
        break
print('Number list: ', user_num_list)
average = sum(user_num_list) / len(user_num_list)
print(average)
if average > 7:
    for i in range(len(user_num_list)):
        user_num_list[i] = user_num_list[i] - 1
print('Number list now: ', user_num_list)
