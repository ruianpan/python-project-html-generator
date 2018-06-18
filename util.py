def lines(file):
    for line in file:
        yield line   # normal ass line yield
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():   #if we have anything in the line
            block.append(line)
        elif block:         #if we have nothing in the line but something in the block
            yield ''.join(block).strip()  #join the block into a string and yield
            block = []
