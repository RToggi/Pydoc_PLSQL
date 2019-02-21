import FileReadWrite

contents = FileReadWrite.ReadWriteobj.file_read("pydocteradata.sql")

foundq = 0
# comments = contents.split("\"\"\"")
# for i in range(len(comments)):
#     comments[i] = comments[i].strip()
txt = ""
print contents
comments = []
for i in contents:
    if "\"\"\"" in i:
        foundq = foundq + 1
    if foundq == 1:
        comments.append(i)
    if foundq == 2:
        foundq = 0

print "Only Comments"

# for i in range(len(comments)):
#     comments[i] = comments[i].strip()
# print comments

FileReadWrite.ReadWriteobj.file_write("Ouput.txt", comments)
print len(comments)
