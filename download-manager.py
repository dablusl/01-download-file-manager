import os
import shutil
import magic

#paths saved in environnement system values in order to be exploited correctly by different script projects
#origin
downloadsPath = os.environ.get('downloads_path')

#destinations
documentsPath = os.environ.get('documents_path')
picturesPath = os.environ.get('pictures_path')
musicPath = os.environ.get('music_path')
videosPath = os.environ.get('videos_path')

#getting all the files of the download folder
files = os.listdir(downloadsPath)

mg = magic.Magic()

for file in files:
    filename, extension = os.path.splitext(file)
    fileSrcPath = os.path.join(downloadsPath, file)
    mimeType = mg.from_file(fileSrcPath)

    extension = extension[1:]

    #application, audio, example, font, image, message, model, multipart, text, and video.
    if 'audio' in mimeType :
        targetPath = musicPath
    elif 'image' in mimeType :
        targetPath = picturesPath
    elif 'video' in mimeType :
        targetPath = videosPath
    elif 'text' in mimeType :
        targetPath = documentsPath
    else :
        continue

    if not os.path.exists( targetPath ) :
        os.makedirs( targetPath )

    fileDesPath = os.path.join(targetPath, file)
       
    shutil.move( fileSrcPath, fileDesPath)