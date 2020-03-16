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
import time, keyboard

def main():
    aux = False

    #Initializate Player object
    player = playerClass.playerClass()

    #Initializate Board
    board = boardClass.boardClass(15, 15)

    #Initializate Random Target and generate a new Random Target
    target = targetClass.targetClass(board.boardWidth, board.boardLength)

    board.updatePlayerStatus(player)


    while True:
        printBoard(board)

        player.updateStatus()
        board.updatePlayerStatus(player)


##        for x in range(225):
##            target.generateRandomTargetOverBoard(board)
##
##            while not aux:
##                if board.checkTargetToBeAWriteablePoint(target):
##                    aux = True
##                    board.setTargetInBoardPoint(target)
##                else:
##                    target.generateRandomTargetOverBoard(board)
##
##            aux = False
##
##            print "\nLoop: %s, total counter targets set: %s\n\ttotal counter targets get: %s" % (x, target.targetsSet, target.targetsGet)
##            printBoard(board)

        time.sleep(1)


def printBoard(board):
    print board.boardMatrix



if __name__ == '__main__':
    main()
