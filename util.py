def lines(file):
    for line in file:
        yield line   # normal ass line yield
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        line_attr = 0 #table ass line
        if line[0]=='\n' or line[0] == ' ' or ord(line[0]) == 9:
            line_attr = 1 #ordinary ass line
        if line.strip():   #if we have anything in the line
            if len(block) == 0:
                if line_attr == 0:
                    block.append('table_note_rp')
            block.append(line)
        elif block:         #if we have nothing in the line but something in the block
            yield ''.join(block).strip()  #join the block into a string and yield
            block = []
