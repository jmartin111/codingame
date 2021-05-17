#!venv/bin/python

line_1 = [i for i in " _     _  _     _  _  _  _  _ "]
line_2 = [i for i in "| |  | _| _||_||_ |_   ||_||_|"]
line_3 = [i for i in "|_|  ||_  _|  | _||_|  ||_| _|"]

CHUNK = 3
DIGITS = len(line_1) // CHUNK
DECODER_RING = {0: [[' ', '_', ' '], ['|', ' ', '|'], ['|', '_', '|']],
                1: [[' ', ' ', ' '], [' ', ' ', '|'], [' ', ' ', '|']],
                2: [[' ', '_', ' '], [' ', '_', '|'], ['|', '_', ' ']],
                3: [[' ', '_', ' '], [' ', '_', '|'], [' ', '_', '|']],
                4: [[' ', ' ', ' '], ['|', '_', '|'], [' ', ' ', '|']],
                5: [[' ', '_', ' '], ['|', '_', ' '], [' ', '_', '|']],
                6: [[' ', '_', ' '], ['|', '_', ' '], ['|', '_', '|']],
                7: [[' ', '_', ' '], [' ', ' ', '|'], [' ', ' ', '|']],
                8: [[' ', '_', ' '], ['|', '_', '|'], ['|', '_', '|']],
                9: [[' ', '_', ' '], ['|', '_', '|'], [' ', '_', '|']]}


def get_digit(index):
    """
    Get the elements of a single digit as represented
    by 3-char chunks from each of the 3 lines (9 total elements)

    :param index: the n-index of the next digit where n represents the
    beginning of the next CHUNK to store
    :returns: a "decoder ring" dictionary for the integers 1-9
    $$$
    """
    # initialize a 2D array to store a single digit line-by-line
    digit = [[] for x in range(CHUNK)]

    digits = [line_1, line_2, line_3]
    for idx, line in enumerate(digits):
        digit[idx] = line[index:index + 3]

    # process the resulting 2D array to generate a real integer
    keys = list(DECODER_RING.keys())
    values = list(DECODER_RING.values())
    return keys[values.index(digit)]


if __name__ == "__main__":
    for i in range(DIGITS):
        print(get_digit(i * CHUNK), end="")
