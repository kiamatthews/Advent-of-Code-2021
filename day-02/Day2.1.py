h = 0
d = 0
instructions = []
with open ("input.txt", "r") as derp:
     for line in derp:
         instructions.append(tuple(line.strip().split(" ")))
for index, tuple in enumerate(instructions):
    x1 = tuple[0]
    x2 = int(tuple[1])
    if x1 == "forward":
        h += x2
    elif x1 == "down":
        d += x2
    elif x1 == "up":
        d -= x2
print (h*d)
