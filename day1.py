import sys

# Part 1
# text = sys.stdin.read()
# depths = text.split('\n')
# greater = 0
# prev = int(depths[0])
# for x in range(1,len(depths)):
#     if int(depths[x]) > prev:
#         greater = greater + 1
#     prev = int(depths[x])
# print(greater)

# Part 2
text = sys.stdin.read()
depths = text.split('\n')
# depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263, 277]
sums = []
for x in range(len(depths) - 2):
    sums.append(int(depths[x]) + int(depths[x + 1]) + int(depths[x + 2]))
greater = 0
for y in range(1, len(sums) - 1):
    if sums[y] > sums[y - 1]:
        greater += 1
print(greater)
# Somehow the answer is not 1636 or 1760 - both are too low