while True:
    hour_period = input('AM or PM? ')
    hour_period = hour_period.upper()
    if hour_period == 'AM' or hour_period == 'PM':
        break
    else:
        print('Please enter AM or PM')
while True:
    hour = int(input('Enter the hour: '))
    if hour > 0 and hour <= 12:
        break
    else:
        print('Hour must be from 1 to 12')
while True:
    minute = int(input('Enter the minute: '))
    if minute >= 0 and minute <= 60:
        break
    else:
        print('Minute must be from 0 to 60')
while True:
    second = int(input('Enter the second: '))
    if second >= 0 and second <= 60:
        break
    else:
        print('Second must be from 0 to 60')
if hour_period == 'AM':
    if hour == 12:
        hour = 0
    else:
        hour = hour
if hour_period == 'PM':
    if hour == 12:
        hour = 12
    else:
        hour = hour + 12
minutes_in_seconds = minute * 60
hours_in_seconds = hour * 3600
total_seconds = hours_in_seconds + minutes_in_seconds + second
print('Seconds since midnight: ', total_seconds)
