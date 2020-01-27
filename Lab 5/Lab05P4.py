import random

list1 = []
for i in range(5):
    random_number = random.randint(1, 9)
    list1.append(random_number)
print('First list:', list1)
list2 = []
for i in range(5):
    random_number2 = random.randint(2, 8)
    list2.append(random_number2)
print('Second list: ', list2)
print('Larger number in each comparison:')
for i in range(5):
    if list1[i] >= list2[i]:
        print(list1[i])
    else:
        print(list2[i])
