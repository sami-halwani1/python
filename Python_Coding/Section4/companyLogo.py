import math
import os
import random
import re
import sys

from collections import Counter, OrderedDict

if __name__ == '__main__':
    s = input()
    
    chars = Counter(s)
    
    sorted_chars = sorted (chars.items(), key= lambda x: (-x[1], x[0]))
    
    for char, count in sorted_chars[:3]:
        print(char, count)