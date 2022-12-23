puzzle_input = open('./inputs/day3_input1.txt', 'r')

def common_char(s):
    s1 = s[:(len(s)//2)]
    s2 = s[(len(s)//2):]

    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                return char1


def priority_of(c):
    priority_base = ord('a')
    if ord(c) >= priority_base:
        return ord(c) - priority_base + 1
    else:
        return ord(c) - 38


total_priority = 0
rucksack = puzzle_input.readline().strip()

while rucksack != '':
    c = common_char(rucksack)
    total_priority += priority_of(c)

    rucksack = puzzle_input.readline().strip()


print(str(total_priority))
