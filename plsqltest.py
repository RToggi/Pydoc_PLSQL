import FileReadWrite
import re

contents = FileReadWrite.ReadWriteobj.file_read("pydocteradata.sql")


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

    FileReadWrite.ReadWriteobj.file_write("Output.txt", comments)
    # print len(comments)


def parse_json():
    pass


def parse_txt():
    print comments
    for i in range(len(comments)):

        if "procedure" in comments[i] or "Procedure" in comments[i]:
            reg_proc = re.compile("Create a procedure(.*)$")
            proc = reg_proc.search(comments[i]).group(1)
            FileReadWrite.ReadWriteobj.file_write("OutputText.txt", "Procedure: " + proc + "\n")
        if "Inserts" in comments[i]:
            reg_insert = re.compile("Inserts the table records into(.*)$")
            ins = reg_insert.search(comments[i]).group(1)
            FileReadWrite.ReadWriteobj.file_write("OutputText.txt",
                                                  "Insert into Table: " + ins + "\n")
        if "param" in comments[i]:
            reg_param = re.compile(":param(.*)$")
            param = reg_param.search(comments[i]).group(1) + "\n"
            FileReadWrite.ReadWriteobj.file_write("OutputText.txt", "Parameter:" + param + "\n")


pick_comments()
parse_txt()
