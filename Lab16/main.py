import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow)

from Ui_gui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.btnOK.setText('OK OK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()

    print('END')