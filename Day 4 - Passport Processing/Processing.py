import re

y = ''
totalValids = 0
with open(r'Day 4 - Passport Processing\Batch.txt', 'r') as f:

    for line in f.read().splitlines():
        y += line + '\n'
        if line == '':
            print('\nThe PassPort is = \n--------------\n' + y)
            x = re.findall('byr|iyr|eyr|hgt|hcl|ecl|pid|cid', y)
            print(str(x) + '\n--------------')
            if 'byr' in x and 'iyr'  in x and 'eyr'  in x and 'hgt'  in x and 'hcl'  in x and 'ecl'  in x and 'pid' in x:
                print('valid')
                totalValids += 1
            
            y = ''
    print('\nThe PassPort is = \n--------------\n' + y)
    x = re.findall('byr|iyr|eyr|hgt|hcl|ecl|pid|cid', y)
    print(str(x) + '\n--------------')
    if 'byr' in x and 'iyr'  in x and 'eyr'  in x and 'hgt'  in x and 'hcl'  in x and 'ecl'  in x and 'pid' in x:
        print('valid')
        totalValids += 1
    print('The Total of Valid Passports are: ' + str(totalValids))


        
        
        