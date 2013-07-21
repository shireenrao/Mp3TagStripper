# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mp3TagStripper.ui'
#
# Created: Sun Jul 21 15:26:03 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(608, 440)
        self.gridLayout_2 = QtGui.QGridLayout(MainDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblDirName = QtGui.QLabel(MainDialog)
        self.lblDirName.setObjectName("lblDirName")
        self.gridLayout_2.addWidget(self.lblDirName, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoadDirectory = QtGui.QPushButton(MainDialog)
        self.btnLoadDirectory.setObjectName("btnLoadDirectory")
        self.horizontalLayout.addWidget(self.btnLoadDirectory)
        self.btnRefresh = QtGui.QPushButton(MainDialog)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout.addWidget(self.btnRefresh)
        self.btnSave = QtGui.QPushButton(MainDialog)
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtGui.QFrame(MainDialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnStripString = QtGui.QPushButton(self.frame)
        self.btnStripString.setObjectName("btnStripString")
        self.horizontalLayout_2.addWidget(self.btnStripString)
        self.optID3 = QtGui.QRadioButton(self.frame)
        self.optID3.setEnabled(True)
        self.optID3.setObjectName("optID3")
        self.horizontalLayout_2.addWidget(self.optID3)
        self.optFile = QtGui.QRadioButton(self.frame)
        self.optFile.setChecked(True)
        self.optFile.setObjectName("optFile")
        self.horizontalLayout_2.addWidget(self.optFile)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(MainDialog)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        MainDialog.setWindowTitle(QtGui.QApplication.translate("MainDialog", "Mp3 Tag Stripper", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDirName.setText(QtGui.QApplication.translate("MainDialog", "Please, load a mp3 directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLoadDirectory.setText(QtGui.QApplication.translate("MainDialog", "Load Directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("MainDialog", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSave.setText(QtGui.QApplication.translate("MainDialog", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStripString.setText(QtGui.QApplication.translate("MainDialog", "Strip", None, QtGui.QApplication.UnicodeUTF8))
        self.optID3.setText(QtGui.QApplication.translate("MainDialog", "ID3", None, QtGui.QApplication.UnicodeUTF8))
        self.optFile.setText(QtGui.QApplication.translate("MainDialog", "File", None, QtGui.QApplication.UnicodeUTF8))

