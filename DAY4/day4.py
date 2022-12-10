# first half
f = open("src.txt")
counter, seccounter = 0, 0
for l in f:
    a = ((l.replace(",", "-")).replace("\n", "")).split("-")
    for i in range(4):
        a[i] = int(a[i])
    firstlength = a[1]-a[0]
    secondlength = a[3]-a[2]
    if firstlength == secondlength:
        if a[0] == a[2]:
            counter += 1
    elif firstlength > secondlength:
        if a[0] <= a[2] and a[1] >= a[3]:
            counter += 1
    else:
        if a[2] <= a[0] and a[3] >= a[1]:
            counter += 1
    # second half
    if a[0] <= a[2] <= a[1] or a[0] <= a[3] <= a[1] or a[2]<= a[0] <= a[3] or a[2] <= a[1] <= a[3]:
        seccounter += 1
print(counter)
print(seccounter)

