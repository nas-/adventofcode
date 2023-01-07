def get_inputs(file):
    with open(file) as file:
        lines = file.readlines()

        inputs = [x.strip().split("|") for x in lines]
        inputs2 = []
        for y in inputs:
            inputs2.append([x.strip().split(" ") for x in y])
    return inputs2


PART_1_LENGTHS = [2, 3, 4, 7]


def process_inputs_part_1(data):
    imput = [x[1] for x in data]
    counter = 0
    for x in imput:
        for y in x:
            if len(y) in PART_1_LENGTHS:
                counter += 1
    return counter


class Row:
    def __init__(self, row):
        self.row = row[0]
        self.output = row[1]
        self.the_one = self._find_1()
        self.the_four = self._find_4()
        self.output_value = self.calculate_output()

    # @property
    def _find_1(self):
        for x in self.row:
            if len(x) == 2:
                return set(x)

    # @property
    def _find_4(self):
        for x in self.row:
            if len(x) == 4:
                return set(x)

    def common_with_one(self, X):
        return len(set(X).intersection(self.the_one))

    def common_with_four(self, X):
        return len(set(X).intersection(self.the_four))

    def decode_word(self, word):
        identified = len(word), self.common_with_one(word), self.common_with_four(word)

        if identified == (2, 2, 2):
            return 1
        elif identified == (5, 1, 2):
            return 2
        elif identified == (5, 2, 3):
            return 3
        elif identified == (4, 2, 4):
            return 4
        elif identified == (5, 1, 3):
            return 5
        elif identified == (6, 1, 3):
            return 6
        elif identified == (3, 2, 2):
            return 7
        elif identified == (7, 2, 4):
            return 8
        elif identified == (6, 2, 4):
            return 9
        elif identified == (6, 2, 3):
            return 0
        else:
            print(f"OMG {identified}")

    def calculate_output(self):
        output = []
        for word in self.output:
            character = self.decode_word(word)
            output.append(str(character))
        return int("".join(output))


k = get_inputs("input")
print(f"Part 1: {process_inputs_part_1(k)}")

rows = [Row(x) for x in k]
print(f"Part 2: {sum(x.output_value for x in rows)}")
pass
