# -*- coding: utf-8 -*-

"""
Module implementing MainDialog.
"""

from PyQt4.QtGui import QDialog, QTreeWidgetItem
from PyQt4.QtCore import pyqtSignature

from Ui_Mp3TagStripper import Ui_MainDialog

class MainDialog(QDialog, Ui_MainDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)

        header = QTreeWidgetItem(["Directory", "Field", "Value"])
        self.treeWidget.setHeaderItem(header)
        self.btnLoadDirectory.setFocus()

    @pyqtSignature("")
    def on_btnLoadDirectory_clicked(self):
        """
        Slot documentation goes here.
        """
        self.loadDir()

    @pyqtSignature("")
    def on_btnRefresh_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnSave_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

    @pyqtSignature("")
    def on_btnStripString_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

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
                audio = MP3(file, ID3=EasyID3)
                myfile = []
                myfile.append(filename)
                mp3file = QTreeWidgetItem(root, myfile)
                for key in sorted(audio.keys()):
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
