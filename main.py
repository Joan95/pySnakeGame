#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:
#
# Author:      JCanalsMascorda
#
# Created:     12/03/2020
# Copyright:   (c) JCanalsMascorda 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import playerClass, boardClass, targetClass
import time

def main():
    aux = False

    #Initializate Player object
    player = playerClass.playerClass()

    #Initializate Board
    board = boardClass.boardClass(15, 15)

    #Initializate Random Target and generate a new Random Target
    target = targetClass.targetClass(board.boardWidth, board.boardLength)


    while True:
        print board.boardMatrix

        for x in range(225):
            target.generateRandomTargetOverBoard(board)

            while not aux:
                if board.checkTargetToBeAWriteablePoint(target):
                    aux = True
                    board.setTargetInBoardPoint(target)
                else:
                    target.generateRandomTargetOverBoard(board)

            aux = False

            printHeader()
            printBoard()

def printBoard():
    print board.boardMatrix

def printHeader():
    print "\nLoop: %s, total counter targets set: %s\n\ttotal counter targets get: %s" % (x, target.targetsSet, target.targetsGet)


if __name__ == '__main__':
    main()
