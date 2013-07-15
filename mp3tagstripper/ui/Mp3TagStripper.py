# -*- coding: utf-8 -*-

"""
Module implementing MainDialog.
"""

from PySide.QtGui import QDialog
#from PyQt4.QtCore import pyqtSignature

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

#    @pyqtSignature("")
    def on_btnLoadDirectory_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

#    @pyqtSignature("")
    def on_btnRefresh_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

#    @pyqtSignature("")
    def on_btnSave_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

#    @pyqtSignature("")
    def on_btnFilterString_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
