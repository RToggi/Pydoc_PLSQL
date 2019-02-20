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
    if "\"\"\"" in i or foundq == 0:
        foundq = 1
        comments.append(i)
    if foundq == 1 and "\"\"\"" in i:
        foundq = 0
        continue
print "Only Comments"
print comments
print len(comments)