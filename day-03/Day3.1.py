diagnostic_report = []
with open ("input.txt", "r") as donk:
     for line in donk:
         diagnostic_report.append(list(line.strip()))
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
    if zero > one:
        gamma = gamma + "0"
    else:
        gamma = gamma + "1"
    ind += 1
ind = 0
for y in range(len(diagnostic_report[0])):
    zero = 0
    one = 0
    for x in diagnostic_report:
        if x[int(ind)] == "0":
            zero += 1
        else:
            one += 1
    if zero < one:
        epsilon = epsilon + "0"
    else:
        epsilon = epsilon + "1"
    ind += 1
print (int(gamma,2)*int(epsilon,2))
