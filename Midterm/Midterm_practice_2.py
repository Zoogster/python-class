five_temps = []
for i in range(5):
    new_temp = float(input('Enter a temperature: '))
    five_temps.append(new_temp)
print('Temperatures entered: ', five_temps)
min_temp = min(five_temps)
print('Lowest temperature: ', min_temp)
max_temp = max(five_temps)
print('Highest temperature: ', max_temp)
average_temp = sum(five_temps) / 5
print('Average temperature: ', average_temp)
hoter_than_average = 0
for i in five_temps:
    if i > average_temp:
        hoter_than_average = hoter_than_average + 1
print('Number of days hotter than the average: ', hoter_than_average)
