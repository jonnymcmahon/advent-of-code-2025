from workshop import read_input


def main():

    input = read_input(2).split(",")

    invalid_ids = set()

    for _range in input:

        # split range
        start_str, end_str = _range.split("-")

        # convert to string and get min + max length
        start, end = int(start_str), int(end_str)
        min_len, max_len = len(start_str), len(end_str)

        # make sure we cover all possible ID lengths
        for length in range(min_len, max_len + 1):

            # loop from 1 length to half length
            for pattern_len in range(1, length // 2 + 1):

                # if there is a remainder - skip this pattern length as it cant repeat fully
                if length % pattern_len != 0:
                    continue

                # set how many repeats are needed to match full length for this pattern length
                repeats = length // pattern_len

                # set low range for this repeating unit
                if pattern_len > 1:
                    low = 10 ** (pattern_len - 1)
                else:
                    low = 1

                # set high range for this repeating unit
                high = 10**pattern_len

                for i in range(low, high):

                    pattern = str(i)
                    number = int(pattern * repeats)

                    if number >= start and number <= end:

                        invalid_ids.add(number)

    print(sum(invalid_ids))


if __name__ == "__main__":
    main()
