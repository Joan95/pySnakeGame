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

'''
Main method por Error Handling
'''
class Error(Exception):

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

class WrongOrUnknownDirection(Error):

    def __init__(self, *args):
        if args:
            try:
                self.message = args[0]
            except IndexError as e:
                pass

    def __str__(self):
        if self.message:
            return('WrongOrUnknownDirection, the direction: {0} is not known. Please assure that the value is between 0 or 3.'.format(self.message))
        else:
            return('WrongOrUnknownDirection has been raised, no further description has been provided.')

class WrongRandomParameters(Error):

    def __init__(self, *args):
        if args:
            try:
                self.message = list(args)
            except IndexError as e:
                pass

    def __str__(self):
        if self.message:
            return('WrongRandomParameters, those values are not valid for calculating the random result between them: {0}. Please assure that the first one is lower than the second one.'.format(self.message))
        else:
            return('WrongRandomParameters has been raised, no further description has been provided.')


class WrongTargetObject(Error):

    def __init__(self, *args):
        if args:
            try:
                self.message = args[0].__module__
            except IndexError as e:
                pass


    def __str__(self):
        if self.message:
            return('WrongTargetObject, the object passed to function is not corresponding to \'targetClass\', it corresponds to \'{0}\''.format(self.message))
        else:
            return('WrongTargetObject has been raised, no further description has been provided.')