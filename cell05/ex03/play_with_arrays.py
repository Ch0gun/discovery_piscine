ori =[4,5,2,1,6,8,1,7]
new = []
for number in ori :
    if number > 5 :
        new.append(number + 2)
news = set(new)
newss = list(news)
print("Original array: " , ori)
print("New array: " , newss)