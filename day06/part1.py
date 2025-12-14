from workshop import read_input


def main():

    input = read_input(6).split("\n")

    operators = input[-1].split()
    rows = input[:-1]

    rows = [row.split() for row in rows]

    i = 0

    grand_total = 0

    while i < len(rows[0]):

        numbers = []

        for row in rows:

            numbers.append(row[i])

        operator = operators[i]

        grand_total += do_calc(numbers, operator)

        i += 1

    print(grand_total)


def do_calc(numbers, operator):

    total = int(numbers.pop(0))

    match operator:
        case "*":

            for number in numbers:
                total *= int(number)

        case "+":

            for number in numbers:
                total += int(number)

    return total


if __name__ == "__main__":
    main()
