class ReadWrite:
    def __init__(self):
        pass

    def file_read(self, fn):
        try:
            f = open(fn, "r")
        except IOError as err:
            print(err.message)
        contents = f.readlines()
        f.close()
        return contents

    def file_write(self, fn, contents):
        try:
            f = open(fn, "w+")
        except IOError as err:
            print(err.message)
        f.writelines(contents)
        f.close()


if __name__ == "__main__":
    ReadWrite.file_write("test.txt", "Hello Test File Write")
