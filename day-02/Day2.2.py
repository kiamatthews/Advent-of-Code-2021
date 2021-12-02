h = 0
d = 0
a = 0
instructions = []
with open ("input.txt", "r") as derp:
     for line in derp:
         instructions.append(tuple(line.strip().split(" ")))
for index, tuple in enumerate(instructions):
    x1 = tuple[0]
    x2 = int(tuple[1])
    if x1 == "forward":
        h += x2
        d += a*x2
    elif x1 == "down":
        a += x2
    elif x1 == "up":
        a -= x2
print (h*d)
