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

    def __init__(self, x = 0, y = 0, speed = 1, size = 2):
        self.x = x
        self.y = y
        self.speed = speed
        self.oldSpeed = self.speed
        self.size = size

    def moveUp(self):
        print("Moving up...")

    def moveDown(self):
        print("Moving down...")

    def moveRight(self):
        print("Moving right...")

    def moveLeft(self):
        print("Moving left...")

    def getSpeed(self):
        return self.speed

    def incrementSpeed(self, value = 1):
        self.speed = self.speed + value
        self.oldSpeed = self.speed

    def stopPlayer(self):
        self.speed = 0

    def playPlayer(self):
        self.speed = self.oldSpeed





