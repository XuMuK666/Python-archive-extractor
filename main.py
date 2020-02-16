from pyunpack import Archive
import magic
f = magic.Magic(uncompress=True)
print(f.from_file("flag.txt"))
Archive('flag.txt').extractall('./')
