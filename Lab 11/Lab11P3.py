input_list = []
for i in range(5):
    num = input('Enter an integer: ')
    try:
        num = int(num)
    except:
        print('Input value cannot be converted to integer')
    else:
        input_list.append(num)

print('Integer list: ', input_list)
