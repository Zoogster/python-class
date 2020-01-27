while True:
    fasting_plasma_glucose = float(
        input('Enter fasting plasma glucose level: '))
    if fasting_plasma_glucose <= 100:
        print('This patient does not have diabetes')
    elif fasting_plasma_glucose > 100 and fasting_plasma_glucose <= 125:
        print('This patient has pre-diabetes')
    elif fasting_plasma_glucose > 125:
        print('This patient has diabetes')
    again = input('Check diabetes for another patient? [y/n] ')
    again = again.lower()
    if again != 'y':
        break
