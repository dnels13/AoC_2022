puzzleInput = open('../inputs/day1_input1.txt', 'r')

currentSum = 0
elfCalorieArray = []
for line in puzzleInput:
    if line == '\n':
        elfCalorieArray.append(currentSum)
        currentSum = 0
    else:
        currentSum += int(line.strip())

print(elfCalorieArray)
print(max(elfCalorieArray))

## PART 2
def top_N_elves(calorieArray, n):
    n_elves_calories = []
    for i in range(0, n):
        n_elves_calories.append(calorieArray.pop(calorieArray.index(max(calorieArray))))

    return n_elves_calories

n = 3
top_n = top_N_elves(elfCalorieArray, n)
print(sum(top_n))
                                
    
