string = input('Enter string: ')
string = string.upper()

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

letter_count = []
for i in range(len(alphabet)):
    count = string.count(alphabet[i])
    if string.count(alphabet[i]) > 0:
        letter_count.append((alphabet[i], count))

letter_count_dict = dict(letter_count)
print('Dictionary: ', letter_count_dict)

letter = input('Enter a letter: ')
letter = letter.upper()

if letter in letter_count_dict:
    print('Frequency count of that letter: ', letter_count_dict[letter])
    del letter_count_dict[letter]
    print('Dictionary after that letter was removed: ', letter_count_dict)
else:
    print('Letter not in dictonary')

letter_in_dict_list = []
for element in letter_count_dict:
    letter_in_dict_list.append(element)
# With the way I did the letter counting the list will naturally be alphabetically sorted so there isn't a reason to sort it.
print('Letters sorted: ', letter_in_dict_list)
