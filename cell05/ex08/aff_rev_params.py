import sys
arg = sys.argv
del sys.argv[0]
arg.reverse()
if len(arg) < 2:
    print("none")
for i in range(len(arg)):
    print(arg[i])
