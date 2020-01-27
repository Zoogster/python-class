class Drone:

    def __init__(self):
        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):
        self.speed = self.speed + 10

    def decelerate(self):
        self.speed = self.speed - 10
        if self.speed < 0:
            self.speed = 0

    def ascend(self):
        self.height = self.height + 10

    def descend(self):
        self.height = self.height - 10
        if self.height < 0:
            self.height = 0
