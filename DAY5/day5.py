# first half
# read header
##not working will be fixed later
f = open("src.txt")
stack = []
lineind = 0
for i in range(8):
    stack.append([])
lineind = 0
for i in f:
    if i.startswith(" 1"):
        break
    chind = -1
    for ch in i:
        if chind%4==0:
            stack[lineind].append(ch)
        chind += 1
    lineind += 1
#placeholders
for i in range(8):
    for l in range(9-len(stack[i])):
        stack[i].append(" ")
f.readline() #skip newln
cargo = stack[:]

print(stack)
for g in range(8):
    for h in range(8):
        cargo[g][h] = stack[h][g]
#for l in f:
#    temp = (l.replace("\n", "")).split(" ")
#    print(temp)
print(stack)
print(cargo)