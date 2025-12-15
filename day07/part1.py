from workshop import read_input


def main():

    input = read_input(7, False).split("\n")

    # convert from str to array
    for i, row in enumerate(input):

        input[i] = list(row)

    beam_row = input.pop(0)

    beams = []

    # find index of beam
    for i, char in enumerate(beam_row):

        # if beam found - set its location in second row
        if char == "S":
            beams.append(i)
            input[0][i] = "|"
            break

    splits = 0

    # loop through each row to find splits
    for y, row in enumerate(input):

        # go through row
        for x, char in enumerate(row):

            # get char above index
            char_above = input[y - 1][x]

            # if character above is a beam, either split or continue
            if char_above == "|":

                # if a splitter, split, if not, continue beam
                if char == "^":
                    splits += 1
                    input[y][x - 1] = "|"
                    input[y][x + 1] = "|"
                else:
                    input[y][x] = "|"

    print(splits)


if __name__ == "__main__":
    main()
