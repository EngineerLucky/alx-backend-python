#!/usr/bin/env python3
'''task 8
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''The function creates a multiplier function.
    '''
    return lambda x: x * multiplier
