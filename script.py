import markup
import os

def GetFileList(dir, fileList):

    for file in os.listdir(dir):
        if file.endswith(".txt"):
            fileList.append(file)
    return fileList

list = GetFileList('C:\play', [])
print(list)
for str in list:
    str = 'C:\play\\'+str
    print(str)
    fin = open(str)
    strr = str.replace('txt', 'html')
    fou = open(strr,'w')
    markup.outside_call(fin, fou)
