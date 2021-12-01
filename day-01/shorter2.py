input = open("input1.txt", "r")
input_list = []
windows = []
for line in input:
    input_list.append(int(line.strip()))
for index, num in enumerate(input_list[:-2]):
    windows.append(num + input_list[index + 1] + input_list[index + 2])
increases = 0
for y, i in enumerate(windows[:-1]):
    if windows[y + 1] > i:
        increases += 1
print (increases)
