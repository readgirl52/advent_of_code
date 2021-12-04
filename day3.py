def part1():
    # input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    lines = []
    with open('input.txt', 'r') as input:
        lines = input.readlines()

    gamma = ''
    epsilon = ''
    ones = 0
    zeros = 0

    for count in range(len(lines[0]) - 1):
        for line in lines:
            if line[count] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma += '0'
            epsilon += '1'
        elif ones > zeros:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '-'
            epsilon += '-'
        ones = 0
        zeros = 0
    print("Gamma:", gamma)
    print("Epsilon:", epsilon)
    print(str(int(gamma, 2) * int(epsilon, 2)))

def part2():
    # input = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    lines = []
    oxy = 0
    co2 = 0
    num_zeros = 0
    num_ones = 0
    zeros = []
    ones = []
    with open('input.txt', 'r') as input:
        lines = input.readlines()
    length = len(lines[0])
    oxy_list = lines
    co2_list = lines
    for count in range(length):
        if len(oxy_list) == 1:
            break
        for val in oxy_list:
            if val[count] == '0':
                num_zeros += 1
                zeros.append(val)
            else:
                num_ones += 1
                ones.append(val)
        if num_zeros > num_ones:
            oxy_list = zeros
        else:
            oxy_list = ones
        num_zeros = 0
        num_ones = 0
        zeros = []
        ones = []
    oxygen = int(oxy_list[0], 2)

    for count in range(length):
        if len(co2_list) == 1:
            break
        for val in co2_list:
            if val[count] == '0':
                num_zeros += 1
                zeros.append(val)
            else:
                num_ones += 1
                ones.append(val)
        if num_ones < num_zeros:
            co2_list = ones
        else:
            co2_list = zeros
        num_zeros = 0
        num_ones = 0
        zeros = []
        ones = []
    co2 = int(co2_list[0], 2)
    print("Oxygen: " + str(oxygen))
    print("CO2: " + str(co2))
    print("Answer: " + str(oxygen * co2))

def main():
    # part1()
    part2()

if __name__ == "__main__":
    main()