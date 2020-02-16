from pyunpack import Archive
import magic
import os
from shutil import copyfile

def rename():
    f = magic.Magic(uncompress=True)
    info = f.from_file("flag.txt")
    fileopen =""
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

    if len(fileopen)>0:
        extract(fileopen)

def extract(fileopen):

    Archive(fileopen).extractall('./test/')
    os.remove(fileopen)
    copyfile("./test/flag.txt", "flag.txt")
    os.remove("./test/flag.txt")

for i in range(100):
    rename()
