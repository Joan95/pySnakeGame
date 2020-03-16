#-------------------------------------------------------------------------------
# Name:        boardClass
# Purpose:
#
# Author:      JCanalsMascorda
#
# Created:     12/03/2020
# Copyright:   (c) JCanalsMascorda 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import targetClass, errorClass as error
import numpy as np

class boardClass():

    def __init__(self, boardWidth = 10, boardLength = 10):
        # Board's X
        self.boardWidth = boardWidth
        # Board's Y
        self.boardLength = boardLength

        # Declare matrix
        self.boardMatrix = np.zeros((self.boardLength,self.boardWidth), dtype = int)


    def setTargetInBoardPoint(self, target):
        if target.__module__ == 'targetClass':
            self.boardMatrix[target.x, target.y] = target.targetTag
            target.incrementTargetsSetCounter()
        else:
            raise error.WrongTargetObject(target)

    def updatePlayerStatus(self, player):
        try:
            self.boardMatrix[player.y, player.x] = player.playerTag
        except IndexError as e:
            print e
            raise IndexError

    def getBoardPoint(self, x, y):
        return self.boardMatrix.item(x, y)


    def checkTargetToBeAWriteablePoint(self, target):
        #TODO: Check if this new target can be added, target.targetPointsSet < boardMatrixWidth * boardMatrixLength
        if target.__module__ == 'targetClass':
            if self.getBoardPoint(target.x, target.y) != target.targetTag:
                return True
            else:
                return False
        else:
            raise error.WrongTargetObject(target)


