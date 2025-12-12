from workshop import read_input


def main():

    input = read_input(3).split("\n")

    total_joltage = 0

    for bank in input:

        # convert string to array
        bank = [int(d) for d in bank]
        length = len(bank)

        # find the first highest digit
        high = -1
        high_index = 0

        for index, battery in enumerate(bank):

            # ignore the last battery as that can't give a 2 digit number
            if index == (length - 1):
                continue

            if int(battery) > int(high):
                high = battery
                high_index = index

        sub_bank = bank[(high_index + 1) :]

        second_digit = max(sub_bank)

        total_joltage += int(str(high) + str(second_digit))

    print(total_joltage)


if __name__ == "__main__":
    main()
