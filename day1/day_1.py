with open("day1/input", encoding="utf-8") as f:
    elves = []
    elf_cals = 0
    for line in f:
        if line != "\n":
            elf_cals += int(line)
        else:
            elves.append(elf_cals)
            elf_cals = 0
    elves.sort()
    print(elves[-1])
    print(sum(elves[-3:]))
