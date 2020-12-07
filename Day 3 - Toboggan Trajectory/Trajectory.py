with open(r'Day 3 - Toboggan Trajectory\Map.txt', 'r') as f:

    tree = '#'
    pos = 0
    amountTrees = 0
    slop = 0
    slopesX = (1, 3, 5, 7, 1)
    slopesY = (1, 1, 1, 1, 2)
    index = 0
    totalMulti = 1
    totalAmountTrees = 0
    for slopeX in slopesX:
        
        print('Slope X -----------' + str(slopeX) + '----------- X epolS')
        print('Slope Y -----------' + str(slopesY[index]) + '----------- Y epolS')
        indexLine = 0
        f.seek(0, 0)
        for line in f.read().splitlines():
            
            if slopesY[index] == 2:
                indexLine += 5
                if str(indexLine).endswith('5'):
                    print(line)
                    if line[pos] == tree:
                        print('hit a tree')
                        amountTrees += 1
                        print()

                    if pos < len(line):
                        pos += slopeX

                    if pos >= len(line):
                        pos -= len(line)
                    print('------------------------------')
            else:
                print(line)
                if line[pos] == tree:
                    print('hit a tree')
                    amountTrees += 1
                    print()

                if pos < len(line):
                    pos += slopeX

                if pos >= len(line):
                    pos -= len(line)
                print('------------------------------')

        print('Total trees this round = ' + str(amountTrees))
        totalMulti *= amountTrees
        totalAmountTrees += amountTrees
        amountTrees = 0
        index += 1
        slop += 1
             
    print('Total trees passed = ' + str(totalAmountTrees))
    print('Total trees passed Multiplied= ' + str(totalMulti))
