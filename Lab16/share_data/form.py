import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg



class FormWindow(qtw.QWidget):
	# cretate custom signal which will cary a string data type data:
	submit = qtc.pyqtSignal(str);

	def __init__(self , msg, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle('My Form')

		# ------------------------- create and atach widgets ------------------------- #
		self.edit = qtw.QLineEdit(msg)
		self.btn_submit = qtw.QPushButton('Submit')

		self.setLayout(qtw.QVBoxLayout())
		self.layout().addWidget(self.edit)
		self.layout().addWidget(self.btn_submit)


		# ---------------------------------- signals --------------------------------- #
		self.btn_submit.clicked.connect(self.onSubmit)


	@qtc.pyqtSlot(bool)
	def onSubmit(self):
		self.submit.emit(self.edit.text())
		self.close()

if __name__=="__main__":
	app = qtw.QApplication(sys.argv);

	window = FormWindow()
	window.show()

	sys.exit(app.exec())
