from FileReadWrite import *
import re
from txtmatch import *
contents = file_read("pydocteradata.sql")


def pick_comments():
    global comments
    found_q = 0
    # print contents
    comments = []
    for i in contents:
        if "\"\"\"" in i:
            found_q = found_q + 1
        if found_q == 1:
            if "\"\"\"" not in i:
                comments.append(i)
        if found_q == 2:
            found_q = 0

    file_write("Output.txt", comments)
    # print len(comments)


def parse_json():
    pass


def parse_txt():
    print comments
    count = 0
    result = ""
    for i in range(len(comments)):

        if "procedure" in comments[i] or "Procedure" in comments[i]:
            proc = create_procedure(comments[i])
            result = result + "\nProcedure: " + proc + "\n"
            count = 0

        if "Inserts" in comments[i]:
            ins = insert_table(comments[i])
            result = result + "\nInsert into Table: " + ins + "\n"
            count = 0
        if "param" in comments[i]:
            if count == 0:
                count = count + 1
                result = result + "\nParameters:\n"
            param = parameter(comments[i])
            result = result + param

    file_write("OutputText.txt", result)


pick_comments()
parse_txt()
