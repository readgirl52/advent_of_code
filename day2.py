# Part 1
# input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
# with open('input.txt', 'r') as input:
#     horizontal = 0
#     depth = 0
#     for line in input:
#         instruction = line.split(' ')
#         if instruction[0] == 'forward':
#             horizontal += int(instruction[1])
#         elif instruction[0] == 'up':
#             depth -= int(instruction[1])
#         elif instruction[0] == 'down':
#             depth += int(instruction[1])
# print("Horizontal:", horizontal)
# print("Depth:", depth)
# print(horizontal * depth)

# Part 2
# input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
with open('input.txt', 'r') as input:
    horizontal = 0
    depth = 0
    aim = 0
    for line in input:
        instruction = line.split(' ')
        if instruction[0] == 'forward':
            horizontal += int(instruction[1])
            depth += (aim * int(instruction[1]))
        elif instruction[0] == 'up':
            aim -= int(instruction[1])
        elif instruction[0] == 'down':
            aim += int(instruction[1])
print("Horizontal:", horizontal)
print("Depth:", depth)
print(horizontal * depth)