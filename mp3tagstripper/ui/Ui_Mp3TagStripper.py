# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/shireenrao/mydev/python/Mp3TagStripper/mp3tagstripper/ui/Mp3TagStripper.ui'
#
# Created: Mon Jul 15 16:13:13 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName(_fromUtf8("MainDialog"))
        MainDialog.resize(608, 440)
        self.gridLayout_2 = QtGui.QGridLayout(MainDialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnLoadDirectory = QtGui.QPushButton(MainDialog)
        self.btnLoadDirectory.setObjectName(_fromUtf8("btnLoadDirectory"))
        self.gridLayout_2.addWidget(self.btnLoadDirectory, 0, 0, 1, 1)
        self.btnRefresh = QtGui.QPushButton(MainDialog)
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))
        self.gridLayout_2.addWidget(self.btnRefresh, 0, 1, 1, 1)
        self.btnSave = QtGui.QPushButton(MainDialog)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout_2.addWidget(self.btnSave, 0, 2, 1, 1)
        self.lblDirName = QtGui.QLabel(MainDialog)
        self.lblDirName.setObjectName(_fromUtf8("lblDirName"))
        self.gridLayout_2.addWidget(self.lblDirName, 1, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(MainDialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btnFilterString = QtGui.QPushButton(self.frame)
        self.btnFilterString.setObjectName(_fromUtf8("btnFilterString"))
        self.horizontalLayout_2.addWidget(self.btnFilterString)
        self.radioButton = QtGui.QRadioButton(self.frame)
        self.radioButton.setEnabled(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.frame)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(MainDialog)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(_translate("MainDialog", "Mp3 Tag Stripper", None))
        self.btnLoadDirectory.setText(_translate("MainDialog", "Load Directory", None))
        self.btnRefresh.setText(_translate("MainDialog", "Refresh", None))
        self.btnSave.setText(_translate("MainDialog", "Save", None))
        self.lblDirName.setText(_translate("MainDialog", "Please, load a mp3 directory", None))
        self.btnFilterString.setText(_translate("MainDialog", "Filter", None))
        self.radioButton.setText(_translate("MainDialog", "ID3", None))
        self.radioButton_2.setText(_translate("MainDialog", "File", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainDialog = QtGui.QDialog()
    ui = Ui_MainDialog()
    ui.setupUi(MainDialog)
    MainDialog.show()
    sys.exit(app.exec_())

