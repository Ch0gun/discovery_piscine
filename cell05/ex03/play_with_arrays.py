ori = [2,8,9,48,8,22,-12,2]
new = []
for number in ori :
    if number > 5 :
        new.append(number + 2)
news = set(new)
newss = list(news)
print("Original array: " , ori)
print("New array: " , newss)