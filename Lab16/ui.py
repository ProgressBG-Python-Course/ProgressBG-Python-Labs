import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class Form(qtw.QWidget):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()

        # attach signals
        self.leUserName.textChanged.connect(self.on_textChanged)
        self.btnSubmit.clicked.connect(self.on_click)
        self.btnCancel.clicked.connect(self.close)
        self.btnClear.clicked.connect(self.on_clear)


    def on_clear(self):
        self.leUserName.clear()
        self.lePass.clear()

    def on_click(self):
        print('Btn was clicked!')
        user_name = self.leUserName.text()
        current_text =self.output.text()
        self.output.setText(f'{current_text}\n{user_name}')

    def on_textChanged(self, text ):
        print(text)


    def setupUI(self):
        self.leUserName = qtw.QLineEdit()
        self.lePass = qtw.QLineEdit()
        self.lePass.setEchoMode(qtw.QLineEdit.EchoMode.Password)
        self.btnSubmit = qtw.QPushButton('Submit')
        self.btnCancel = qtw.QPushButton('Cancel')
        self.btnClear = qtw.QPushButton('Clear')
        self.output = qtw.QLabel()

        buttons_layout = qtw.QHBoxLayout()
        buttons_layout.addWidget(self.btnSubmit)
        buttons_layout.addWidget(self.btnCancel)
        buttons_layout.addWidget(self.btnClear)

        main_layout = qtw.QFormLayout()
        main_layout.addRow('User name:', self.leUserName)
        main_layout.addRow('pass:', self.lePass)
        main_layout.addRow(buttons_layout)
        main_layout.addRow(self.output)

        self.setLayout(main_layout)

        self.setWindowTitle('Registration')
        self.setGeometry(300, 200,400, 200)
        self.show()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv);

    window = Form()
    window.show()

    sys.exit(app.exec())
