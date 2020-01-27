class Drone:

    def __init__(self):
        self.__speed = 0.0
        self.__height = 0.0

    def accelerate(self):
        self.__speed = self.__speed + 10

    def decelerate(self):
        self.__speed = self.__speed - 10
        if self.__speed < 0:
            self.__speed = 0

    def ascend(self):
        self.__height = self.__height + 10

    def descend(self):
        self.__height = self.__height - 10
        if self.__height < 0:
            self.__height = 0

    def __str__(self):
        return 'Speed: ' + str(self.__speed) + ' ' + 'Hight: ' + str(self.__height)
