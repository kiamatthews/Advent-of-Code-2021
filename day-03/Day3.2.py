diagnostic_report = []
with open ("input.txt", "r") as donk:
     for line in donk:
         diagnostic_report.append(list(line.strip()))
diagnostic_report_again = diagnostic_report
ind = 0
for a in range(len(diagnostic_report[0])):
    while len(diagnostic_report) > 1:
        zero = 0
        one = 0
        for x in diagnostic_report:
            if x[int(ind)] == "0":
                zero += 1
            else:
                one += 1
        if zero > one:
            diagnostic_report = [i for i in diagnostic_report if i[int(ind)] == "0"]
        elif zero < one:
            diagnostic_report = [i for i in diagnostic_report if i[int(ind)] == "1"]
        elif zero == one:
            diagnostic_report = [i for i in diagnostic_report if i[int(ind)] == "1"]
        ind += 1
o2 = ''.join(map(str, diagnostic_report[0]))
ind = 0
for a in range(len(diagnostic_report_again[0])):
    while len(diagnostic_report_again) > 1:
        zero = 0
        one = 0
        for x in diagnostic_report_again:
            if x[int(ind)] == "0":
                zero += 1
            else:
                one += 1
        if zero < one:
            diagnostic_report_again = [i for i in diagnostic_report_again if i[int(ind)] == "0"]
        elif zero > one:
            diagnostic_report_again = [i for i in diagnostic_report_again if i[int(ind)] == "1"]
        elif zero == one:
            diagnostic_report_again = [i for i in diagnostic_report_again if i[int(ind)] == "0"]
        ind += 1
co2 = ''.join(map(str, diagnostic_report_again[0]))
print (int(o2,2)*int(co2,2))
