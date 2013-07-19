
from PySide.QtCore import *
from PySide.QtGui import *
import sys
from ui import Ui_Mp3TagStripper
import os
#from mp3lib.mp3utils import Mp3FileInfo
from mp3lib import mp3utils

__appname__ = "Mp3 Tag Stripper"


class MainDialog(QDialog, Ui_Mp3TagStripper.Ui_MainDialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.mp3dir = ''

        header = QTreeWidgetItem(["Directory", "Field", "Value"])
        self.treeWidget.setHeaderItem(header)
        self.btnLoadDirectory.setFocus()
        self.btnLoadDirectory.clicked.connect(self.loadDir)
        self.btnStripString.clicked.connect(self.stripString)

    def stripString(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, __appname__, "Nothing to strip!")
        if self.treeWidget.topLevelItemCount() == 0:
            QMessageBox.warning(self, __appname__, "No Directory loaded to cleanup")

    def loadDir(self):
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        d = QFileDialog.getExistingDirectory(self,
                                             __appname__ + " Open Directory",
                                             os.getcwd(), flags)
        if d != '':
            self.treeWidget.clear()
            self.lblDirName.setText(d)
            self.mp3dir = d
            mp3zList = self.getAllMp3DetailsList(d)
            #header = QTreeWidgetItem(["Directory", "Field", "Value"])
            #self.treeWidget.setHeaderItem(header)
            rootdir = []
            rootdir.append(os.path.basename(d))
            root = QTreeWidgetItem(self.treeWidget, rootdir)
            for mp3file in mp3zList:
                myfile = []
                myfile.append(mp3file.filename)
                mp3node = QTreeWidgetItem(root, myfile)
                for key in sorted(mp3file.id3tags.keys()):
                    if key != 'APIC:':
                        mp3detail = QTreeWidgetItem(mp3node)
                        mp3detail.setText(0, "")
                        mp3detail.setText(1, key)
                        if isinstance(unicode(mp3file.id3tags[key]),
                                      (list, tuple)):
                            mp3detail.setText(2,
                                              unicode(mp3file.id3tags[key][0]))
                        else:
                            mp3detail.setText(2, unicode(mp3file.id3tags[key]))
            self.treeWidget.resizeColumnToContents(0)
            #pointListBox.show()

    def getAllMp3DetailsList(self, path):
        mp3DetailsList = []
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in files:
                    filename = os.path.join(root, name)
                    if filename.lower().endswith('.mp3'):
                        mp3obj = mp3utils.mp3FileInfo(filename)
                        mp3DetailsList.append(mp3obj)
        return mp3DetailsList


app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
sys.exit(app.exec_())
