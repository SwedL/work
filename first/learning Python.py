
from zipfile import ZipFile


def sizeof_fmt(num):
    for x in ['B', 'KB', 'MB', 'GB']:
        if num < 1024.0:
            return round(num), x
        num /= 1024.0
    return round(num), 'TB'

with ZipFile('D:/desktop.zip') as zfi:
    info = list(zfi.namelist())
    files_info = zfi.infolist()
    for i in range(len(info)):
        print(info[i], *sizeof_fmt(files_info[i].file_size))


