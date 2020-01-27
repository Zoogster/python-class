course_list = []
while True:
    choice = input('Enter A to add course, D to drop course, and E to exit: ')
    choice = choice.upper()
    if choice == 'A':
        course_to_add = input('Enter course to add: ')
        if course_to_add in course_list:
            print('You are already registered in that course')
            continue
        else:
            course_list.append(course_to_add)
            print('Course added')
            course_list.sort()
            print('Courses registered: ', course_list)
    elif choice == 'D':
        course_to_drop = input('Enter course to drop: ')
        course_to_drop = course_to_drop.upper()
        if course_to_drop in course_list:
            course_list.remove(course_to_drop)
            print('Course dropped')
            print('Courses registered: ', course_list)
        else:
            print('You are not registered in that course')
    elif choice == 'E':
        break
