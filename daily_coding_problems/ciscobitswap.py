import pandas as pd
import numpy as np

## Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped, and so on.

### For example, 10101010 should be 01010101

def bit_swap(x):
    start = list(str(x))
    middle = list(zip(np.arange(len(start)), start))
    #print(middle)
    end = []
    for idx,int_ in middle:
        if idx%2==0:
            end.append(middle[idx+1])
        else: end.append(middle[idx-1])
    middle_2 = [j for i,j in end]
    
    return int(''.join(map(str,middle_2)))
    
print((bit_swap(1234)))