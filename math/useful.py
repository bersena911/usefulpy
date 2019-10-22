'''
Most useful functions from math
'''


def is_negative(k):
    '''
    Determines if given k is negative
    :param k:
    :return: bool: True if k is negative, False otherwise
    '''
    if k < 0:
        return True
    return False


def is_x(x, k):
    '''
    Determines if given k is x
    :param x:
    :param k:
    :return: bool: True if k is x, False otherwise
    '''
    if k == x:
        return True
    return False


def is_ten(k):
    '''
    Determines if k equals ten
    :param k:
    :return: bool: True if k equals ten, False otherwise
    '''
    return is_x(10, k)
