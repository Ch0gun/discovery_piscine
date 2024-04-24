#!/usr/bin/env python3
import sys
arg = sys.argv
num = len(arg) - 1
print("parameters: " , num)
del arg[0]
for i in range(len(arg)) :
    print(arg[i] , ":" , len(arg[i]))