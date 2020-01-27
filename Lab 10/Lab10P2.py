def main():
    string = input('Enter string: ')
    string = string.upper()

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    letter_count = []
    for i in range(len(alphabet)):
        count = string.count(alphabet[i])
        if string.count(alphabet[i]) > 0:
            letter_count.append((alphabet[i], count))

    for element in letter_count:
        print(element[0], element[1])


main()
