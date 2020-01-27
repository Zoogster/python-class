room_length = float(input('Enter room length: '))
room_width = float(input('Enter room width: '))
room_height = float(input('Enter room height: '))
room_volume = room_length * room_width * room_height
btu_needed = room_volume * 3.5
print('BTU needed for this room:', format(btu_needed, ".2f"))
