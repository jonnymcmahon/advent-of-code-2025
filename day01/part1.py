from workshop import read_input


def main():

    data = read_input(1)

    # starting position of 50
    pos = 50

    # init zero count
    zero_count = 0

    for instruction in data:

        # isolate distance from direction
        distance = int(instruction[1:])

        # if it's more than 100, find the remainder from 100
        if distance > 100:

            distance = distance % 100

            if distance == 0:
                continue

        # apply correct direction
        if instruction[0] == "L":

            distance = -distance

        # apply turns
        pos = pos + distance

        # if it went below zero, set up to 99
        if pos < 0:
            pos = 100 - abs(pos)

        # if it went above 100, find remainder and use that
        if pos >= 100:
            pos = pos % 100

        # if it stopped at zero, increment
        if pos == 0:
            zero_count += 1

    print(zero_count)


if __name__ == "__main__":
    main()
