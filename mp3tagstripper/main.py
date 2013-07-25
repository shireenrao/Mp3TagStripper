
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
        self.id3flag = False
        self.fileflag = False

        header = QTreeWidgetItem(["Directory", "Field", "Value"])
        self.treeWidget.setHeaderItem(header)
        self.btnLoadDirectory.setFocus()
        self.btnLoadDirectory.clicked.connect(self.loadDir)
        self.btnStripString.clicked.connect(self.stripString)
        self.btnRefresh.clicked.connect(self.refresh)
        self.btnSave.clicked.connect(self.save)

    def save(self):
        if (not self.fileflag) and (not self.id3flag):
            QMessageBox.warning(self, __appname__, "Nothing to Save!")
            return

        msg = ''
        if self.fileflag:
            self.saveFiles()
            msg = "Saving filenames complete!"
            self.fileflag = False

        if self.id3flag:
            self.saveID3Tags()
            if msg:
                msg += "\nSaving id3 tags complete!"
            else:
                msg = "Saving id3 tags complete!"
            self.id3flag = False

        self.reloadDir()
        QMessageBox.information(self, __appname__, msg)

    def saveID3Tags(self):

        params = {}
        params['mp3files'] = self.getAllMp3sList(self.lblDirName.text())
        params['expr'] = self.id3Str2Strip
        params['compare'] = ''
        params['print'] = ''

        mp3utils.savecleantags(params)

    def saveFiles(self):

        params = {}
        params['mp3files'] = self.getAllMp3sList(self.lblDirName.text())
        params['expr'] = self.fileStr2Strip
        params['compare'] = ''
        params['print'] = ''

        mp3utils.rename(params)

    def stripString(self):
        _expression = self.lineEdit.text()
        if _expression == "":
            QMessageBox.warning(self, __appname__, "Nothing to strip!")
            return
        if self.treeWidget.topLevelItemCount() == 0:
            QMessageBox.warning(self, __appname__, "No Directory loaded to cleanup")
            return
        #setup flags to see what is being stripped
        msg = ''
        if self.optID3.isChecked():
            self.id3flag = True
            self.id3Str2Strip = _expression
            msg = "ID3 Stripping complete!"
        if self.optFile.isChecked():
            self.fileflag = True
            self.fileStr2Strip = _expression
            msg = "Filename Stripping complete!"

        #it = QTreeWidgetItemIterator(self.treeWidget)
        #while it.value():
        #    if it.value().text(0) != '':
        #        print it.value().text(0)
        #    it += 1
        if self.fileflag:
            for mp3file in self.mp3zList:
                if not mp3file.fileisclean:
                    mp3file.cleanFilename(self.fileStr2Strip)

        if self.id3flag:
            for mp3file in self.mp3zList:
                if not mp3file.id3isclean:
                    mp3file.cleanTags(self.id3Str2Strip)
        self.reloadDir()
        QMessageBox.information(self, __appname__, msg)

    def loadDir(self):
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        d = QFileDialog.getExistingDirectory(self,
                                             __appname__ + " Open Directory",
                                             os.getcwd(), flags)
        if d != '':
            self.lblDirName.setText(d)
            self.mp3dir = d
            self.mp3zList = self.getAllMp3DetailsList(d)
            self.reloadDir()

    def refresh(self):
        d = self.lblDirName.text()
        self.mp3zList = self.getAllMp3DetailsList(d)
        self.fileflag = False
        self.id3flag = False
        self.reloadDir()

    def reloadDir(self):
        path = self.lblDirName.text()
        self.treeWidget.clear()
        #header = QTreeWidgetItem(["Directory", "Field", "Value"])
        #self.treeWidget.setHeaderItem(header)
        rootdir = []
        rootdir.append(os.path.basename(path))
        root = QTreeWidgetItem(self.treeWidget, rootdir)
        for mp3file in self.mp3zList:
            myfile = []
            if self.fileflag:
                myfile.append(mp3file.cleanfile)
            else:
                myfile.append(mp3file.filename)
            mp3node = QTreeWidgetItem(root, myfile)
            if self.id3flag:
                for key in sorted(mp3file.cleanid3Tags.keys()):
                    if key != 'APIC:':
                        mp3detail = QTreeWidgetItem(mp3node)
                        mp3detail.setText(0, "")
                        mp3detail.setText(1, key)
                        if isinstance(unicode(mp3file.cleanid3Tags[key]),
                                        (list, tuple)):
                            mp3detail.setText(2,
                                                unicode(mp3file.cleanid3Tags[key][0]))
                        else:
                            mp3detail.setText(2, unicode(mp3file.cleanid3Tags[key]))
            else:
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

    def getAllMp3sList(self, path):
        mp3sList = []
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in files:
                    filename = os.path.join(root, name)
                    if filename.lower().endswith('.mp3'):
                        mp3sList.append(filename)
        return mp3sList

app = QApplication(sys.argv)
form = MainDialog()
form.show()
form.raise_()
sys.exit(app.exec_())
