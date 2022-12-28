import pdb

puzzle_input = open('../inputs/day5_input.txt', 'r')

def initialize_stacks(file):
    crate_stacks = [[] for i in range(0,9)]
    itemRow = file.readline().strip('\n')
    while '[' in itemRow:
        for i in range(0,9):
            item = itemRow[(i*4)+1]
            if item != ' ':
                crate_stacks[i].append(item)

        itemRow = file.readline().strip('\n')

    reverse_stacks(crate_stacks)
    return crate_stacks


def reverse_stacks(crate_stacks):
    for stack in crate_stacks:
        stack.reverse()

#Part 1
def move_crates(n, stacks, stack_A, stack_B):
     for i in range(0, n):
        crate = stacks[stack_A].pop()
        stacks[stack_B].append(crate)

#Part 2
def move_n_crates(n, stacks, stack_A_index, stack_B_index):
    #pdb.set_trace()
    stack_A = stacks[stack_A_index]
    crates_to_be_moved = stacks[stack_A_index][(len(stack_A)-n):]
    stacks[stack_B_index]+= crates_to_be_moved
    stacks[stack_A_index] = stacks[stack_A_index][:(len(stack_A)-n)]

def scrape_top(stacks):
    top_items = ""
    for i in range(0, len(stacks)):
        top_items += stacks[i].pop()
    
    return top_items


crate_stacks = initialize_stacks(puzzle_input)
puzzle_input.readline() # <- empty line before directions start
direction = puzzle_input.readline().strip()

while direction != '':
    n_end = direction.find('from') - 1
    n = int(direction[5:n_end])
    stack_A = int(direction[direction.find('from') + 5]) - 1
    stack_B = int(direction[direction.find('to') + 3]) - 1
    #move_crates(n, crate_stacks, stack_A, stack_B) # Part 1
    move_n_crates(n, crate_stacks, stack_A, stack_B)

    direction = puzzle_input.readline()

top_items = scrape_top(crate_stacks)
print(top_items)




