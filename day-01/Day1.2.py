#!/usr/bin/python
input = open("input1.txt", "r")
input_list_raw = list(input.readlines())
input_list = []
windows = []
for x in input_list_raw:
    input_list.append(int(x.strip('\n')))
for index, num in enumerate(input_list[:-2]):
    windows.append(num + input_list[index + 1] + input_list[index + 2])
increases = 0
for y, i in enumerate(windows[:-1]):
    if windows[y + 1] > i:
        increases += 1
print (increases)
