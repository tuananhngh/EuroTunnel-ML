path_d1 = "/Users/Slaton/Downloads/D_1.blochet"
with open(path_d1, encoding='ISO-8859-1') as f:
    lines = f.readlines()

example_line = lines[32]


def read_number_line(some_line):
    return [float(s) for s in some_line.split()]
