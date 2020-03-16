#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      JCanalsMascorda
#
# Created:     16/03/2020
# Copyright:   (c) JCanalsMascorda 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Import own modules
import errorClass

# Import python modules
import random

def randomBetweenTwoLimits(lowerRange, upperRange):
    if lowerRange < upperRange:
        point = random.randint(lowerRange, upperRange)
        return point
    else:
        raise errorClass.WrongRandomParameters(lowerRange, upperRange)


