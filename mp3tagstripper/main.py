
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from ui import Ui_Mp3TagStripper
import os
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

__appname__ = "Mp3 Tag Stripper"

class MainDialog(QDialog, Ui_Mp3TagStripper.Ui_MainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.mp3dir = ''

        header = QTreeWidgetItem(["Directory", "Field", "Value"])
        self.treeWidget.setHeaderItem(header)
        #self.treeWidget.setColumnWidth(25)
        self.btnLoadDirectory.setFocus()
        self.btnLoadDirectory.clicked.connect(self.loadDir)


    def loadDir(self):
        dir = "."
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        d = QFileDialog.getExistingDirectory(self, __appname__ +
                                             " Open Directory", os.getcwd()
                                             , flags)
        if d != '':
            self.treeWidget.clear()
            self.lblDirName.setText(d)
            self.mp3dir = d
            fileList = self.getmp3list(d)
            header = QTreeWidgetItem(["Directory", "Field", "Value"])
            self.treeWidget.setHeaderItem(header)
            rootdir = []
            rootdir.append(os.path.basename(d))
            root = QTreeWidgetItem(self.treeWidget, rootdir)
            for file in fileList:
                filename = os.path.basename(file)
                #print filename
                audio = MP3(file, ID3=EasyID3)
                myfile = []
                myfile.append(filename)
                mp3file = QTreeWidgetItem(root, myfile)
                for key in sorted(audio.keys()):
                    #print key + ' ' + audio[key]
                    mp3detail = QTreeWidgetItem(mp3file)
                    mp3detail.setText(0,"")
                    mp3detail.setText(1,key)
                    mp3detail.setText(2,audio[key][0])
            self.treeWidget.resizeColumnToContents(0)
            #pointListBox.show()

    def getmp3list(self, path):
        fileList = []
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in files:
                    filename = os.path.join(root,name)
                    if filename.lower().endswith('.mp3'):
                        fileList.append(filename)
        return fileList


app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
sys.exit(app.exec_())
