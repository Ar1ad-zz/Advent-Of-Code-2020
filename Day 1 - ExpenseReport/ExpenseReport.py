with open(r'C:\Users\sebastian.aho\Desktop\AoC\ExpenseReport\Report.txt', 'r') as report:

    temp = report.read().splitlines()

    # - Part 1 -

    # for line in temp:
    #     tempnum = 2020 - int(line)
    #     print("2020 - " + str(line) + " = " + str(tempnum))
    #     for i in temp:
    #         if str(tempnum) in i:
    #             if i == str(tempnum):
    #                 out = tempnum * int(line)
    #                 print("out = " + str(out))


    # - Part 2 -
    for line in temp:
        templine = line
        for i in temp:
            templine2 = i
            for x in temp:
                if int(templine) + int(templine2) + int(x)== 2020:
                    out = int(templine) * int(templine2) * int(x)
                    print(str(out))