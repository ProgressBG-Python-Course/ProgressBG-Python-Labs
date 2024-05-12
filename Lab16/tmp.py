import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
# Import the compiled UI module
from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Set up the user interface from Designer
        self.setupUi(self)
        # Connect signals and slots here, or setup other initializations

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())