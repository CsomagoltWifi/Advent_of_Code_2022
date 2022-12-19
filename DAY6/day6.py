f = open("src.txt")
line = f.readline()
def difflenght(a):
    for i in range(len(line)):
        lst = line[i:i+a:]
        s = set(lst)
        if len(s) == a:
            return i+a
print(difflenght(4))
print(difflenght(14))