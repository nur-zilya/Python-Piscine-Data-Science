import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        has_header = True
        text = self.check_file(has_header)
        return text

    def check_file(self, has_header):
        if not os.access(self.path, os.R_OK):
            raise ValueError("File cannot be read")
        with open(self.path, "r") as f:
            lines = [line.rstrip() for line in f]
        if (len(lines) < 1):
            raise ValueError("Size of the file is too small")
        if lines[0] == "0,1" or lines[0] == "1,0":
            has_header = False
        if len(lines[0].split(',')) != 2:
            raise ValueError("Header is incorrect")
        r_lines = []
        if has_header:
            r_lines = lines[1:]
        else:
            r_lines = lines
        for line in r_lines:
            if line != "0,1" and line != "1,0":
                raise ValueError("Data in the file is incorrect")
        res = []
        for line in r_lines:
            strs = line.split(',')
            numbers = []
            for number in strs:
                numbers.append(int(number))
            res.append(list(numbers))
        return res

    class Calculations:
        def counts(self, data):
            heads = 0
            tails = 0
            for pair in data:
                heads += pair[0]
                tails += pair[1]
            return heads, tails
        def fractions(self, heads, tails):
            first = heads * 100 / (heads + tails)
            second = tails * 100 / (heads + tails)
            return first, second

if __name__ == '__main__':

    if len(sys.argv) != 2:
        raise ValueError("No input file")
    res = Research(sys.argv[1])
    print(res.file_reader())
    data = res.Calculations()
    calc = data.counts(res.file_reader())
    print(calc[0], calc[1])
    frac = data.fractions(calc[0], calc[1])
    print(frac[0], frac[1])

