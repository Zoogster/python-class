import random

set1 = set()
for i in range(5):
    random_num = random.randint(1, 10)
    set1.add(random_num)
print('set1: ', set1)

set2 = set()
for i in range(5):
    random_num = random.randint(1, 10)
    set2.add(random_num)
print('set2: ', set2)

sets_union = set1 | set2
print('Union of set1 and set2: ', sets_union)

odd_sets_union = {num for num in sets_union if num % 2 == 1}
print('Odd numbers in union of set1 and set2: ', odd_sets_union)

sets_intersection = set1 & set2
print('Intersection of set1 and set2: ', sets_intersection)

sets_symmetric = set1 ^ set2
print('Symmetrical difference of set1 and set2: ', sets_symmetric)
