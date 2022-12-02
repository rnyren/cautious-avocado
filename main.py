list = []
elfCalories = []
calories = 0


with open("01\input.txt","r") as fdata:
    for line in fdata:
        v = line.rstrip()
        if v == "":
             elfCalories.append(calories)
             print (f"elf {len(elfCalories)} : {calories} calories")
             calories = 0;
        else:
            calories = calories + int(v)

maxCalories = max(elfCalories)
elfId = elfCalories.index(maxCalories) + 1 #list index location + 1 for 0 list start
print (f"maximum calories = {maxCalories} for elf {elfId}")

'''--- Part Two ---
By the time you calculate the answer to the Elves' question, 
they've already realized that the Elf carrying the most Calories of 
food might eventually run out of snacks.
To avoid this unacceptable situation, the Elves would instead 
like to know the total Calories carried by the top three 
Elves carrying the most Calories. 
That way, even if one of those Elves runs out of snacks, they still have two backups.
In the example above, the top three Elves are the fourth Elf (with 24000 Calories), 
then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). 
The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. 
How many Calories are those Elves carrying in total?'''

elfCalories.sort()
total = sum(elfCalories[-3:])
print(f"calories for top 3 elves total {total}")