#!/usr/bin/env python3
ori =[4,5,2,1,6,8,1,7]
new = []
for number in ori :
    if number > 5 :
        new.append(number + 2)
print("Original array: " , ori)
print("New array: " , new)