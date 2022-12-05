score = 0
def chint(ch):
    if ch.islower():
        return ord(ch)-96
    else:
        return ord(ch)-38

f = open("src.txt")
for i in f:
    # first half
    first, sec, index,  = [], [], 1
    for a in i:
            if index <= len(i)/2 and a not in first:
                first.append(a)
            if index > len(i)/2 and a not in sec:
                sec.append(a)
            index += 1
    for b in first:
        if b in sec:
            score += chint(b)
            break
f.close()

print(score)
index, secscore = 0, 0
g = open("src.txt")
# second half
for l in g:

    if index == 0:
        first, pos = [], []
        index += 1
        for c in l:
            first.append(c)
    elif index == 1:
        index += 1
        for c in l:
            if c in first:
                pos.append(c)
    else:
        index = 0
        for c in l:
            if c in pos:
                secscore += chint(c)
                break
    #print(first, pos, secscore)
print(secscore)
