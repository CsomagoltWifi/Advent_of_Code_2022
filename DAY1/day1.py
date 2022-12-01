# first half
f = open("scr.txt")
sumlist = []
i = 0
for x in f:
    if x == "\n":
        sumlist.append(i)
        i = 0
    else:
        i += int(x)
print(max(sumlist))
# second half
sortedlist = sorted(sumlist, reverse=True)
top3sum = 0
for i in range(3):
    top3sum += sortedlist[i]
print(top3sum)
