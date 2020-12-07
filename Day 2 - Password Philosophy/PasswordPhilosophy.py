import re

numOfCorrectPass = 0
numOfCorrectPass2 = 0
with open('Day 2 - Password Philosophy\Passwords.txt', 'r') as f:
    


    # - Part 1 -

    # for line in f.read().splitlines():
        
    #     splitLine = re.split('[-, ,:]', line)
    #     password = splitLine[4]
    #     range1 = splitLine[0]
    #     range2 = splitLine[1]
    #     letter = splitLine[2]
        
    #     print('\n-------------------------------part1--------------------------------------------\n')
    #     print('split = ' + str(splitLine))
    #     print('password = ' + str(password))
    #     print('range1 = ' + str(range1))
    #     print('range2 = ' + str(range2))
    #     print('letter = ' + str(letter))

    #     numOfLetters = 0        

    #     for i in password:
    #         if i == letter:
    #             numOfLetters += 1
    #     if numOfLetters >= int(range1) and numOfLetters <= int(range2):
    #             print('password is correct')
    #             numOfCorrectPass += 1
    #     print('numOfLetters = ' + str(numOfLetters))
    #     print('Part 1 Correct Passwords = ' + str(numOfCorrectPass))


    # - Part 2 -

    for line in f.read().splitlines():
        
        splitLine = re.split('[-, ,:]', line)
        password = splitLine[4]
        range1 = int(splitLine[0])
        range2 = int(splitLine[1])
        letter = splitLine[2]
        
        print('\n-------------------------------part2--------------------------------------------\n')
        print('split = ' + str(splitLine))
        print('password = ' + str(password))
        print('range1 = ' + str(range1))
        print('range2 = ' + str(range2))
        print('letter = ' + str(letter))

        print('l1 = ' + password[range1 - 1 ])
        print('l2 = ' + password[range2 - 1 ])

        numOfLetters = 0        

        if bool(password[range1 - 1] == letter) ^ bool(password[range2 - 1] == letter):
            print('password is correct')
            numOfCorrectPass2 += 1
        print('Part 2 Correct Passwords = ' + str(numOfCorrectPass2))