import sys
arg = sys.argv
if len(arg) - 1 != 1 :
    print("none")
elif len(arg) -1 == 1 :
    same = input("What was the parameter? ")
    if same == arg[1] :
        print("Good job!")
    else :
        print("Nope, sorry...")