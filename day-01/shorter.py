input_list = []
input = open("input1.txt", "r")
for line in input:
    input_list.append(int(line.strip()))
increases = 0
for y, i in enumerate(input_list[:-1]):
    if input_list[y + 1] > i:
        increases += 1
print (increases)
