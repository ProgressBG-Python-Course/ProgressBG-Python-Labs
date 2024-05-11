import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('')
        self.setupUI()
        self.show()

    def setupUI(self):
        main_layout = qtw.QFormLayout()
        self.leUserName = qtw.QLineEdit()
        self.lePass = qtw.QLineEdit()
        self.lePass.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        main_layout.addRow('User name:', self.leUserName)
        main_layout.addRow('pass:', self.lePass)
        self.setLayout(main_layout)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = MainWindow()

    sys.exit(app.exec())
