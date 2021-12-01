#!/usr/bin/python
input = open("input1.txt", "r")
input_list_raw = list(input.readlines())
input_list = []
counter = 0
increases = 0
for x in input_list_raw:
    input_list.append(int(x.strip('\n')))
for x in input_list[:-1]:
    if input_list[int(counter) + 1] > x:
        increases += 1
    counter +=1
print (increases)
