import os
import shutil

#download path saved in environnement system values in order to be exploited correctly by different script projects
path = os.environ.get('downloads_path')

files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists( path + '/' + extension ) :
        shutil.move( path + '/' + file, path + '/' + extension + '/' + file )
    else :
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)