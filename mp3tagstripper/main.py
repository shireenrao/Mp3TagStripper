from PySide import QtCore, QtGui
import sys
from ui.Mp3TagStripper import MainDialog

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form = MainDialog()
    form.show()
    form.raise_()
    sys.exit(app.exec_())
