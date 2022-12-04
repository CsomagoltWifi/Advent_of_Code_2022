# AX = rock(1), BY = paper(2), CZ= scissor(3), A<B<C<A
# first half
base = {"X" : 1, "Y" : 2, "Z" : 3}
mark = {"A" : "X", "B" : "Y", "C" : "Z"}
score, rescore = 0, 0
f = open("src.txt")
for x in f:
    opp, me = x.split()
    score += base[me]
    if mark[opp] == me:
        score += 3
    elif (opp == "A" and me == "Y") or (opp == "B" and me == "Z") or (opp == "C" and me == "X"):
        score += 6
    # second half
    if me == "Y":
        rescore += base[mark[opp]] + 3
    elif me == "Z":
        if opp == "C":
            rescore += 7
        else:
            rescore += base[mark[opp]] + 7
    else:
        if opp == "A":
            rescore += 3
        else:
            rescore += base[mark[opp]] -1

print(score)
print(rescore)
