import os
import shutil

path = 'C:/Users/Matt/Desktop/City of Mist/Characters'

base_char_sheet = 'C:/Users/Matt/Desktop/City of Mist/Characters/City of Mist RPG - Character Sheets'
character_name = input('Enter character name: ')
char_sheet_named = f'{base_char_sheet}' + ' - ' + character_name
print(f'Path for new character sheet is: {char_sheet_named}.pdf')
correct = input('Is that correct [y] or [n]: ')
correct = correct.lower()

if correct == 'y':
    copying = shutil.copyfile(base_char_sheet + '.pdf',
                              char_sheet_named + '.pdf')
else:
    print('Then try again')
