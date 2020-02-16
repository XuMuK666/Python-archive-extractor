from pyunpack import Archive
import magic
import os
from shutil import copyfile
try:
    import lzma
except ImportError:
    from backports import lzma


def xz(fileopen):
    f = open('./test/flag.txt', 'w+b')
    f.write(lzma.open(fileopen).read())
    f.close()


def rename():
    f = magic.Magic(uncompress=True)
    info = f.from_file("flag.txt")
    print(info)
    fileopen =""
    flag = False
    if info.find("POSIX") !=-1:
        fileopen="flag.tar.gz"
        copyfile("flag.txt", fileopen)
        os.remove("flag.txt")

    if info.find("archive data") !=-1:
        fileopen="flag.zip"
        copyfile("flag.txt", fileopen)
        os.remove("flag.txt")

    if info.find("bzip2 compressed data") !=-1:
        fileopen="flag.bz2"
        copyfile("flag.txt", fileopen)
        os.remove("flag.txt")

    if info.find("gzip compressed") !=-1:
        fileopen="flag.tar.gz"
        copyfile("flag.txt", fileopen)
        os.remove("flag.txt")

    if info.find("XZ compressed data") !=-1:
        fileopen="flag.tar.xz"
        copyfile("flag.txt", fileopen)
        os.remove("flag.txt")
        f = open('flag.txt', 'w+b')
        f.write(lzma.open('flag.tar.xz').read())
        f.close()
        os.remove(fileopen)
        flag = True
        fileopen=""

    if len(fileopen)>0:
        extract(fileopen)
    if flag:
        rename()

def extract(fileopen):
    try:
        Archive(fileopen).extractall('./test/')
    except:
        xz(fileopen)
    os.remove(fileopen)
    try:
        copyfile("./test/flag", "./test/flag.txt")
        os.remove("./test/flag")
        
    copyfile("./test/flag.txt", "flag.txt")
    os.remove("./test/flag.txt")

for i in range(100):
    rename()
