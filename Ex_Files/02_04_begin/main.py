NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

#efficient but def more bug prone
i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

#"for in loop" is less bug prone -> "for each name in NAMES, then print name"
for name in NAMES:
    print(name)

#iterating through two collections at once, zip() doesn't build a new list in memory
for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

#"for each name in reversed(NAMES), then print name"
for name in reversed(NAMES):
    print(name)

#iterate a range that is not build in memory, don't have an indication of what iteration you're on
for i in range(5):
    print(i)

#enumerate
    for i, name in enumerate(NAMES):
        print(f"{i} {name}")

