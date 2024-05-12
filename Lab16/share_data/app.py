import sys
from PyQt6 import QtWidgets as qtw
from main_window import MainWindow

if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec())