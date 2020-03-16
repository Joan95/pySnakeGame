#-------------------------------------------------------------------------------
# Name:        playerClass
# Purpose:
#
# Author:      JCanalsMascorda
#
# Created:     12/03/2020
# Copyright:   (c) JCanalsMascorda 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class playerClass():

    def __init__(self, speed = 1, direction = 2, size = 4, namePlayer = ''):
        self.y = list()
        self.x = list()
        self.speed = speed
        self.oldSpeed = self.speed
        self.direction = direction
        self.size = size
        self.namePlayer = namePlayer
        self.playerTag = 99

        for i in range(0, size):
            self.y.append(0)
            self.x.append(0)


    def updateStatus(self):
        for i in range(self.size-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 0:
            # Moving up
            self.y[0] = self.y[0] - self.speed

        elif self.direction == 1:
            # Moving right
            self.x[0] = self.x[0] + self.speed

        elif self.direction == 2:
            # Moving down
            self.y[0] = self.y[0] + self.speed

        elif self.direction == 3:
            # Moving left
            self.x[0] = self.x[0] - self.speed

        else:
            raise WrongOrUnknownDirection()

    def moveUp(self):
        self.direction = 0

    def moveDown(self):
        self.direction = 1

    def moveRight(self):
        self.direction = 2

    def moveLeft(self):
        self.direction = 3

    def getSpeed(self):
        return self.speed

    def incrementSpeed(self, value = 1):
        self.speed = self.speed + value
        self.oldSpeed = self.speed

    def setPlayerName(self, name):
        self.name = name

    def stopPlayer(self):
        self.speed = 0

    def playPlayer(self):
        self.speed = self.oldSpeed





