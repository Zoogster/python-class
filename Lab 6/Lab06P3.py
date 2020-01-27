import random

list1 = []
for i in range(10):
    random_number = random.randint(1, 15)
    list1.append(random_number)
tuple1 = tuple(list1)
print('Tuple of 10 random numbers: ', tuple1)
tuple2 = tuple1[:3]
print('Tuple of first 3 numbers: ', tuple2)
tuple3 = tuple1[-3:]
print('Tuple of last 3 numbers: ', tuple3)
tuple4 = tuple2 + tuple3
print('Two tuples concatenated: ', tuple4)
list_of_tuple4 = list(tuple4)
list_of_tuple4.sort()
sorted_tuple4 = tuple(list_of_tuple4)
print('Two tuples concatenated and sorted: ', sorted_tuple4)
