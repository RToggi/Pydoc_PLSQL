import FileReadWrite

contents = FileReadWrite.ReadWriteobj.file_read("pydocteradata.sql")


def pick_comments():
    foundq = 0
    # print contents
    comments = []
    for i in contents:
        if "\"\"\"" in i:
            foundq = foundq + 1
        if foundq == 1:
            if "\"\"\"" not in i:
                comments.append(i)
        if foundq == 2:
            foundq = 0

    FileReadWrite.ReadWriteobj.file_write("Ouput.txt", comments)
    # print len(comments)


def parse_json():
    pass


def parse_txt():
    pass


pick_comments()
parse_txt() 