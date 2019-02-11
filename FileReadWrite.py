class ReadWrite:
    def __init__(self):
        pass

    def file_read(self, fn):
        """Returns list of lines stored in a file"""
        try:
            f = open(fn, "r")
        except IOError as err:
            print(err.message)
        contents = f.readlines()
        f.close()
        return contents

    def file_write(self, fn, contents):
        """Writes onto the lines"""
        try:
            f = open(fn, "w+")
        except IOError as err:
            print(err.message)
        print (f.writelines(contents))
        f.close()


if __name__ == "__main__":
    a = ReadWrite()
    # a.file_write("test.txt", "Hello Test File Write")
    # print(a.file_read("test.txt"))
