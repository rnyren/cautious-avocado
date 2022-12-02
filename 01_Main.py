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