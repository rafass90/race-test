class Reader:
    @staticmethod
    def read_file(filename):
        f = open(filename, "r")
        return f


class Writer:
    @staticmethod
    def write_file(filename, content):
        file = open(filename, 'w+')
        file.truncate(0)
        file.write(str(content))
        file.close()
