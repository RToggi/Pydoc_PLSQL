import re


def create_procedure(inp):
    reg_proc = re.compile('Create a procedure(.*)$')
    return reg_proc.search(inp).group(1)


def insert_table(inp):
    reg_insert = re.compile('Inserts the table records into(.*)$')
    return reg_insert.search(inp).group(1)


def parameter(inp):
    reg_param = re.compile(":param(.*)$")
    return reg_param.search(inp).group(1) + "\n"
