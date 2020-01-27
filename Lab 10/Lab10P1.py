def main():
    input_time = input('Enter time [hh:mm:ss]: ')

    num_of_colons = 0
    for e in input_time:
        if e == ':':
            num_of_colons = num_of_colons + 1

    if num_of_colons != 2:
        print('Must separate hour, minute and second with colons')
        return

    hour = input_time[:2]
    minute = input_time[3:5]
    sec = input_time[6:]

    if len(hour) is not 2:
        print('Hour must be a 2-digit number.')
        return
    elif len(minute) is not 2:
        print('Minute must be a 2-digit number.')
        return
    elif len(sec) is not 2:
        print('Second must be a 2-digit number.')
        return

    hour_num = float(hour)
    minute_num = float(minute)
    sec_num = float(sec)

    if hour_num < 0 or hour_num > 23:
        print('Hour must be a 2-digit number between 0 and 23.')
        return
    elif minute_num < 0 or minute_num > 59:
        print('Minute must be a 2-digit number between 0 and 59')
    elif sec_num < 0 or sec_num > 59:
        print('Second must be a 2-digit number between 0 and 59')
        return
    time_no_colon = hour + minute + sec
    print('Time with colons removed: ', time_no_colon)


main()
