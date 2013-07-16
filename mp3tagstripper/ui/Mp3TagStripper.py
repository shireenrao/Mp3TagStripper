# -*- coding: utf-8 -*-

"""
Module implementing MainDialog.
"""

from PySide.QtCore import Slot
from PySide.QtGui import QDialog,  QFileDialog

from .Ui_Mp3TagStripper import Ui_MainDialog
import os

class MainDialog(QDialog, Ui_MainDialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @Slot()
    def on_btnLoadDirectory_clicked(self):
        """
        Slot documentation goes here.
        """
        flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        d = QFileDialog.getExistingDirectory(self, "Open Directory", os.getcwd(), flags)
        #path, _ = QFileDialog.getOpenFileName(self, "Open File", os.getcwd())
        self.lblDirName.setText(d)
    
    @Slot()
    def on_btnRefresh_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @Slot()
    def on_btnSave_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @Slot()
    def on_btnFilterString_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @Slot()
    def on_btnStripString_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
