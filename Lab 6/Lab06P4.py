list1 = [2, 5, 7, 8]
list2 = [1, 2]
part_a = [(x * 2) + 1 for x in list1]
print('Part a: ', part_a)
part_b = [x + 1 for x in list1 if x % 2 == 0]
print('Part b: ', part_b)
part_c = [[x, x + 1] for x in list1]
print('Part c: ', part_c)
part_d = [[x, y] for x in list1 for y in list2]
print('Part d: ', part_d)
part_e = [[x+list2[0], x+list2[1]] for x in list1]
print('Part e: ', part_e)
