puzzle_input = open('../inputs/day3_input1.txt', 'r')

def common_char(bags):
    common_items = set(bags[0])
    for bag in bags[1:]:
        common_items &= set(bag)

    return common_items.pop()


def priority_of(c):
    priority_base = ord('a')
    if ord(c) >= priority_base:
        return ord(c) - priority_base + 1
    else:
        return ord(c) - 38

# ------ PART 1 ------
total_priority = 0
rucksack = puzzle_input.readline().strip()

while rucksack != '':
    bags = []
    bags.append(rucksack[:len(rucksack)//2])
    bags.append(rucksack[len(rucksack)//2:])
    c = common_char(bags)
    total_priority += priority_of(c)

    rucksack = puzzle_input.readline().strip()


print(str(total_priority))
puzzle_input.close()

# ------ PART 2 ------

puzzle_input = open("../inputs/day3_input1.txt", "r")
rucksack = puzzle_input.readline().strip()
bags = []
total_priority = 0

while rucksack != '':
    bags.append(rucksack)
    
    if len(bags) == 3:
        c = common_char(bags)
        total_priority += priority_of(c)
        bags = []
    
    rucksack = puzzle_input.readline().strip()

print(str(total_priority))
puzzle_input.close()
