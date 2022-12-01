def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data.split('\n')