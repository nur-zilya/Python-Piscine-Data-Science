import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        text = self.check_file()
        return text

    def check_file(self):
        if not os.access(self.path, os.R_OK):
            raise ValueError("File cannot be read")
        with open(self.path, "r") as f:
            lines = [line.rstrip() for line in f]
        if (len(lines) < 2):
            raise ValueError("Size of the file is too small")
        if lines[0] == "0,1" or lines[0] == "1,0" \
            or len(lines[0].split(',')) != 2:
            raise ValueError("Header is incorrect")
        for line in lines[1:]:
            if line != "0,1" and line != "1,0":
                raise ValueError("Data in the file is incorrect")
        return "\n".join(lines)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("No input file")
    m = Research(sys.argv[1])
    print(m.file_reader())
