#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    subStrings = s.split()
    result = []
    
    for string in subStrings:
        if string[0].isalpha():
            string = string.capitalize()
        result.append(string)

    String = " ".join(result)
 
    return String

print(solve("q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"))