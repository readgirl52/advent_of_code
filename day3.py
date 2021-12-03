input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
# with open('input.txt','r') as input:
gamma = ''
epsilon = ''
ones = 0
zeros = 0

for count in range(len(input[0])):
    for num in input:
        if num[count] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
    ones = 0
    zeros = 0
print(str(int(gamma, 2) * int(epsilon, 2)))
