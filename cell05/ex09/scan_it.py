import sys , re
arg = sys.argv
del arg[0]
if len(arg) != 2 :
    print("none")
word = sys.argv[0]
text = sys.argv[1]
print(text.count(word))