diagnostic_report = []
with open ("input_sample.txt", "r") as donk:
     for line in donk:
         diagnostic_report.append(list(line.strip()))
diagnostic_report_again = diagnostic_report
ind = 0
for a in range(len(diagnostic_report[0])):
    while len(diagnostic_report) > 1:
        zero = 0
        one = 0
        for x in diagnostic_report:
            #print (x[int(ind)])
            if x[int(ind)] == "0":
                zero += 1
            else:
                one += 1
        #print (zero)
        #print (one)
        print (diagnostic_report)

        if zero > one:
            print ("There are more zeroes.")
            diagnostic_report = [i for i in diagnostic_report if i[int(ind)] == "0"]
            print (diagnostic_report)
            #for y in diagnostic_report:
            #    print ("The bit in position " + str(ind) + " is " + y[int(ind)])
            #    if y[int(ind)] == "1":
            #        print (str(y) + "should be removed from the list")
                    #diagnostic_report.remove(y)
        elif zero < one:
            print ("There are more ones.")
            diagnostic_report = [i for i in diagnostic_report if i[int(ind)] == "1"]
            print (diagnostic_report)
            #for y in diagnostic_report:
            #    print ("The bit in position " + str(ind) + " is " + y[int(ind)])
            #    if y[int(ind)] == "0":
            #        print (str(y) + "should be removed from the list")
                    #diagnostic_report.remove(y)
        elif zero == one:
            print ("There are an equal number of zeros and ones.")
            diagnostic_report = [i for i in diagnostic_report if i[int(ind)] == "1"]
            print (diagnostic_report)
        #print (diagnostic_report)
        print (" -- End of Cycle Through Index Position " + str(ind) + "--")
        ind += 1

print ("The final Oxygen number is " + str(diagnostic_report))

ind = 0
for a in range(len(diagnostic_report_again[0])):
    while len(diagnostic_report_again) > 1:
        zero = 0
        one = 0
        for x in diagnostic_report_again:
            #print (x[int(ind)])
            if x[int(ind)] == "0":
                zero += 1
            else:
                one += 1
        #print (zero)
        #print (one)
        print (diagnostic_report_again)

        if zero < one:
            print ("There are fewer zeroes.")
            diagnostic_report_again = [i for i in diagnostic_report_again if i[int(ind)] == "0"]
            print (diagnostic_report_again)
            #for y in diagnostic_report:
            #    print ("The bit in position " + str(ind) + " is " + y[int(ind)])
            #    if y[int(ind)] == "1":
            #        print (str(y) + "should be removed from the list")
                    #diagnostic_report.remove(y)
        elif zero > one:
            print ("There are fewer ones.")
            diagnostic_report_again = [i for i in diagnostic_report_again if i[int(ind)] == "1"]
            print (diagnostic_report_again)
            #for y in diagnostic_report:
            #    print ("The bit in position " + str(ind) + " is " + y[int(ind)])
            #    if y[int(ind)] == "0":
            #        print (str(y) + "should be removed from the list")
                    #diagnostic_report.remove(y)
        elif zero == one:
            print ("There are an equal number of zeros and ones.")
            diagnostic_report_again = [i for i in diagnostic_report_again if i[int(ind)] == "0"]
            print (diagnostic_report_again)
        print (" -- End of Cycle Through Index Position " + str(ind) + "--")
        ind += 1

print ("The final CO2 number is " + str(diagnostic_report_again))
