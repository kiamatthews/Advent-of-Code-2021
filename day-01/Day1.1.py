#!/usr/bin/python
input = open("input1.txt", "r")
input_list_raw = list(input.readlines())
input_list = []
increases = 0
for x in input_list_raw:
    input_list.append(int(x.strip('\n')))
for y, i in enumerate(input_list[:-1]):
    if input_list[y + 1] > i:
        increases += 1
print (increases)
