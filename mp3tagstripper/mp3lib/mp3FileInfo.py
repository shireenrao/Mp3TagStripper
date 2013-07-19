import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3 #@UnresolvedImport
from mutagen.id3 import ID3, TOPE, TDRC, TPE2, TPE1, TALB, TRCK, TIT2, TCON, TENC, COMM, TCOM #@UnresolvedImport

class Mp3FileInfo:

    def __init__(self, filename, filter=None):
        self.filepath = filename
        self.filename = os.path.basename(filename)
        self.foldername = os.path.split(os.path.split(filename)[0])[1]
        self.id3tags = MP3(filename, ID3=EasyID3)

