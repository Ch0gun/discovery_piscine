#!/usr/bin/env python3
first_num = int(input("Enter the first number : "))
sec_num = int(input("Enter the second number : "))
ans = first_num * sec_num
print(first_num , "x" , sec_num , "=" , ans)
if ans > 0 :
    print("This result is positive.")
elif ans < 0 :
    print("This result is negative.")
else :
    print("This result is both positive and negative.")