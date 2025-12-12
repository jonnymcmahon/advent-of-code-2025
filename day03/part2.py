from workshop import read_input


def main():

    input = read_input(3).split("\n")

    total_joltage = 0

    for bank in input:

        start_index = 0
        high_index = 0

        joltage = ""

        # convert string to array
        bank = [int(d) for d in bank]

        # run until all digits are found
        while len(joltage) < 12:

            # define a sub_bank, constrained by numbers after most recent digit found and how many digits are left to find
            start_index += high_index
            end_index = (-11 + len(joltage)) or None

            sub_bank = bank[start_index:end_index]

            # find high and its index
            high, high_index = find_highest_digit(sub_bank)

            # add high to joltage value
            joltage += str(high)

            # increment start_index by 1 to avoid repeats
            start_index += 1

        total_joltage += int(joltage)

    print(total_joltage)


def find_highest_digit(batteries):

    high = -1
    high_index = 0

    for index, battery in enumerate(batteries):

        if int(battery) > int(high):
            high = battery
            high_index = index

    return high, high_index


if __name__ == "__main__":
    main()
