import random

list1 = []
for i in range(5):
    new_num = random.randint(5, 40)
    list1.append(new_num)
print('List 1: ', list1)

list2 = []
for i in range(5):
    new_num = random.randint(10, 35)
    list2.append(new_num)
print('List 2: ', list2)

list3 = list1[:2] + list2[2:5]
print('List 3: ', list3)

list4 = list2[:2] + list1[2:5]
print('List 4: ', list4)

list5 = []
for i in range(5):
    if list3[i] >= list4[i]:
        list5.append(list3[i])
    else:
        list5.append(list4[i])
print('List 5: ', list5)

list6 = []
for i in range(5):
    if list3[i] <= list4[i]:
        list6.append(list3[i])
    else:
        list6.append(list4[i])
print('List 6: ', list6)

larger_than_30 = [x for x in list5 if x > 30]
print('Elements in list5 larger than 30: ', larger_than_30)

nested_list = [[x*2 for x in list5], [x*3 for x in list6]]
print('List of lists: ', nested_list)
