#將檔案名稱去除空格(用在sox使用方便)
# os.rename(要修改的文件名,修改成的文件名)
# os.join()
import os
path = os.getcwd() 
fileList = os.listdir(path)
currectnamelist=[] 
for i in fileList:
    tmpname = i.replace(" ","")
    currectnamelist.append(tmpname)
count = 0
for fname in os.listdir(path):
    targetname = os.path.join(path,fname)
    os.rename(targetname, os.path.join(path, currectnamelist[count]))
    count = count + 1     