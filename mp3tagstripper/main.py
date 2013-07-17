
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from ui import Ui_Mp3TagStripper
import os

__appname__ = "Mp3 Tag Stripper"

class MainDialog(QDialog, Ui_Mp3TagStripper.Ui_MainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.mp3dir = ''

        self.btnLoadDirectory.setFocus()
        self.btnLoadDirectory.clicked.connect(self.loadDir)


    def loadDir(self):
        dir = "."
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        d = QFileDialog.getExistingDirectory(self, __appname__ +
                                             " Open Directory", os.getcwd()
                                             , flags)
        if d != '':
            self.lblDirName.setText(d)
            self.mp3dir = d
            fileList = self.getmp3list(d)
            #pointListBox = QTreeWidget()
            header = QTreeWidgetItem(["Directory","Filename", "Field", "Detail"])
            self.treeWidget.setHeaderItem(header)
            rootdir = []
            rootdir.append(os.path.basename(d))
            root = QTreeWidgetItem(self.treeWidget, rootdir)
            for file in fileList:
                filename = os.path.basename(file)
                print filename
                myfile = []
                myfile.append(filename)
                mp3file = QTreeWidgetItem(root, myfile)
                mp3detail = QTreeWidgetItem(mp3file, ["Field", "some detail"])
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
