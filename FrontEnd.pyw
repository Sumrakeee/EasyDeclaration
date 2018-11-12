from PyQt5 import QtWidgets
import csv
from Design import Ui_MainWindow
import webbrowser
from PyQt5.QtWidgets import (QLabel, QMessageBox)
import sys

class mywindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.savequestion)

	def savequestion(self, event):
		reply = QMessageBox.question(self,'Сохранение','Вы уверены?')
		if reply == QMessageBox.Yes:
			pass
		else:
			pass

def main():
	app = QtWidgets.QApplication([])
	application = mywindow()
	application.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()