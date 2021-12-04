diagnostic_report = []
with open ("input_sample.txt", "r") as donk:
     for line in donk:
         diagnostic_report.append(list(line.strip()))
#print (diagnostic_report)
gamma = ""
epsilon = ""

ind = 0
for y in range(len(diagnostic_report[0])):
    zero = 0
    one = 0
    for x in diagnostic_report:
        if x[int(ind)] == "0":
            zero += 1
        else:
            one += 1
    print (zero, "zeroes")
    print (one, "ones")
    if zero > one:
        gamma = gamma + "0"
    else:
        gamma = gamma + "1"
    ind += 1
print (gamma)

ind = 0
for y in range(len(diagnostic_report[0])):
    zero = 0
    one = 0
    for x in diagnostic_report:
        if x[int(ind)] == "0":
            zero += 1
        else:
            one += 1
    print (zero, "zeroes")
    print (one, "ones")
    if zero < one:
        epsilon = epsilon + "0"
    else:
        epsilon = epsilon + "1"
    ind += 1
print (epsilon)
print (int(gamma,2))
print (int(epsilon,2))
