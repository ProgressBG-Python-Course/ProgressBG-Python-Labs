import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from form import Ui_Form


class Window(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.btnOK.clicked.connect(self.on_click)

    def on_click(self):
        print('clicked')
        user_name = self.leUserName.text()
        print(user_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = Window()
    win.show()

    sys.exit(app.exec())
