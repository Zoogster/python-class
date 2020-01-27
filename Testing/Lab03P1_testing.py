hour_period = input('AM or PM? ')
hour_period = hour_period.upper()
hour = int(input('Enter the hour: '))
minuite = int(input('Enter the minuite: '))
second = int(input('Enter the second: '))
if hour_period == 'AM':
    if hour == 12:
        hours = 0
    elif hour < 12:
        hours = hour
if hour_period == 'PM':
    if hour == 12:
        hours = 12
    if hour < 12:
        hours = hour + 12
minuites_in_seconds = minuite * 60
hours_in_seconds = hours * 3600
total_seconds = hours_in_seconds + minuites_in_seconds + second
print('Seconds since midnight: ', total_seconds)


# and hour == 12:
#   hours = 0
# elif hour_period == 'AM' and hour < 12:
# hours = hour
# elif hour_period == 'PM' and hour == 12:
#    hours = 12
# elif hour_period == 'PM' and hour < 12:
#    hours = hour + 12
# minuites_in_seconds = minuite * 60
# hours_in_seconds = hours * 3600
# total_seconds = hours_in_seconds + minuites_in_seconds + second
# print('Seconds since midnight: ', total_seconds)
