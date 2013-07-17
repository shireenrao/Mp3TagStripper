import sys
from PyQt4.QtGui import QApplication
from ui.Mp3TagStripper import MainDialog

def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    form.raise_()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
