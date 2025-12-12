from pathlib import Path

path = Path(__file__).parent / "input.txt"

with open(path, "r") as file:

    data = file.read()

    data = data.split("\n")[:-1]

# starting position of 50
pos = 50

# init zero count
zero_count = 0

for instruction in data:

    # isolate distance from direction
    distance = int(instruction[1:])
    dir = instruction[0]

    # get full and partial turns
    full, partial = divmod(distance, 100)
    zero_count += full

    # apply direction
    if dir == "L":
        partial = -partial

    # get next position
    next_pos = pos + partial

    if pos != 0:
        if dir == "L" and next_pos <= 0:
            zero_count += 1
        elif dir == "R" and next_pos >= 100:
            zero_count += 1

    pos = next_pos % 100

print(zero_count)
