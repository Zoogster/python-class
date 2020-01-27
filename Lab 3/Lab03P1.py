hour_period = input('AM or PM? ')
hour_period = hour_period.upper()
hour = int(input('Enter the hour: '))
minute = int(input('Enter the minute: '))
second = int(input('Enter the second: '))
if hour_period == 'AM':
    if hour == 12:
        hour = 0
    else:
        hour = hour
if hour_period == 'PM':
    if hour == 12:
        hour = hour
    else:
        hour = hour + 12
minutes_in_seconds = minute * 60
hours_in_seconds = hour * 3600
total_seconds = hours_in_seconds + minutes_in_seconds + second
print('Seconds since midnight: ', total_seconds)
