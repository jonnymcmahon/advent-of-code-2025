from workshop import read_input


def main():

    input = read_input(6).split("\n")

    operators = input[-1]
    rows = input[:-1]

    i = 0
    width = 0
    calc = False

    grand_total = 0

    while i < len(rows[0]):

        # loop to check for spaces
        for row in rows:

            # if its the last problem it wont have a trailing space so just set calc to True and break
            if i == len(row) - 1:
                calc = True
                break

            # break if non space found
            if row[i] != " ":
                calc = False
                break

            # if break did not trigger we can calc
            calc = True

        if calc is True:

            # get start index of problem
            start_index = i - width
            end_index = i

            # if its the last problem add 1 to end index to make sure we capture it all
            if i == len(rows[0]) - 1:
                end_index += 1

            numbers = []

            for row in rows:

                numbers.append(row[start_index:end_index])

            grand_total += do_calc(numbers, operators[start_index])

            calc = False
            width = -1

        i += 1
        width += 1

    print(grand_total)


def do_calc(numbers, operator):

    # set index to end
    i = len(numbers[0]) - 1

    parsed_numbers = []

    while i >= 0:

        # create blank string for parsed number
        parsed_num = ""

        # loop through rows to get i of each row
        for number in numbers:

            num = number[i]

            # if it's a space, ignore it
            if num == " ":
                continue

            # otherwise, add it to number
            parsed_num += num

        # add it to parsed_numbers
        parsed_numbers.append(parsed_num)

        i -= 1

    # get first num
    total = int(parsed_numbers.pop(0))

    # do calc
    match operator:
        case "*":

            for number in parsed_numbers:
                total *= int(number)

        case "+":

            for number in parsed_numbers:
                total += int(number)

    return total


if __name__ == "__main__":
    main()
