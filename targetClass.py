#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      JCanalsMascorda
#
# Created:     12/03/2020
# Copyright:   (c) JCanalsMascorda 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import common

class targetClass:

    def __init__(self, boardWidth, boardLength):
        self.x = 0
        self.y = 0
        self.targetTag = 88
        self.totalTargets = boardWidth * boardLength
        self.targetsSet = 0
        self.targetsGet = 0

    def generateRandomTargetOverBoard(self, board):
        self.x = common.randomBetweenTwoLimits(0, board.boardWidth - 1)
        self.y = common.randomBetweenTwoLimits(0, board.boardLength - 1)

    def incrementTargetsSetCounter(self):
        self.targetsSet = self.targetsSet + 1

