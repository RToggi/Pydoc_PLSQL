def file_write(fn, contents):
    """Writes onto the lines"""
    try:
        f = open(fn, "a+")
    except IOError as err:
        print(err.message)
    print (f.writelines(contents))
    f.close()
    pass


def file_read(fn):
    """Returns list of lines stored in a file"""
    try:
        f = open(fn, "r")
    except IOError as err:
        print(err.message)
    contents = f.readlines()
    f.close()
    return contents

