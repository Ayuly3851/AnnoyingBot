# -*- coding: utf-8 -*-
# RUN SCRIPT

from javascript import require, On
mineflayer = require('mineflayer')

from PyQt5.QtWidgets import (QMainWindow, QApplication)

from ui_draw import Ui_MainWindow
from ui_func_setup import Ui_Function

import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.uif = Ui_Function()
		self.uif.setupUiFunction(self)

	@property
	def gripSize(self):
		return self._gripSize
	def setGripSize(self, size):
		self.uif.setGripSize(self, size)
	def updateGrips(self):
		self.uif.updateGrips(self)
	def resizeEvent(self, event):
		self.uif.resizeEvent(self, event)
	def mousePressEvent(self, event):
		self.uif.mousePressEvent(self, event)
	def mouseMoveEvent(self, event):
		self.uif.mouseMoveEvent(self, event)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec())
