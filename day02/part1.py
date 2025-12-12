from workshop import read_input


def main():

    input = read_input(2).split(",")

    total = 0

    for _range in input:

        # split range
        start, end = _range.split("-")

        # loop through from start to end
        for i in range(int(start), int(end) + 1):

            i = str(i)
            length = len(i)

            # if it isnt even in length, skip it
            if length % 2 != 0:
                continue

            # get half way point
            half_index = int(length / 2)

            # separate front and back half of number
            prefix = i[:half_index]
            suffix = i[half_index:]

            # if they match, add to total
            if prefix == suffix:

                total += int(i)

    print(total)


if __name__ == "__main__":
    main()
