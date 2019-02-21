import FileReadWrite
import re
contents = FileReadWrite.ReadWriteobj.file_read("pydocteradata.sql")


def pick_comments():
    global comments
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

    FileReadWrite.ReadWriteobj.file_write("Output.txt", comments)
    # print len(comments)


def parse_json():
    pass


def parse_txt():
    print comments
    regproc = re.compile("procedure(.*)$")
    for i in range(len(comments)):

        if "procedure" in comments[i] or "Procedure" in comments[i]:
            proc = regproc.search(comments[i]).group(1)

    print "Procedure: " + proc

pick_comments()
parse_txt()