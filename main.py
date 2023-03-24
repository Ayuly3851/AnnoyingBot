from javascript import require, On
mineflayer = require('mineflayer')
import time, uuid, sys, threading, os, psutil

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from ui_draw import Ui_MainWindow
from ui_func_setup import Ui_Function

from ui_function import UIFunction
from Utility import Utility, SideGrip

__import__('os').system('cls')

"""
thread with gui:
 https://stackoverflow.com/questions/22340230/python-pyqt-how-run-while-loop-without-locking-main-dialog-window
 https://realpython.com/python-pyqt-qthread/
 https://www.google.com/search?q=pyqt+run+while+loop+without+not+responding&oq=pyqt+run+while+loop+without+not+re&aqs=chrome.2.69i57j33i160l4.25736j0j7&sourceid=chrome&ie=UTF-8
"""

class MainWindow(QMainWindow):
	# _gripSize = 2
	# signal = pyqtSignal(str)
	def __init__(self):
		super().__init__()
		self.uif = Ui_Function()
		self.uif.setupUiFunction(self)

		# self.uifunc = UIFunction(self)
		
		self.utility = Utility()

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


	### CONTROLBOT ###
	def spawnbot(self):
		_bot = Bot()
		host = self.uic.ip_tb_2.text()
		port = self.uic.port_sp_2.value()
		botname = self.uic.usrname_tb.text()
		ver = self.uic.ver_cb_2.currentText()
		login_msg = self.uic.login_msg_tb.text()
		left_msg = self.uic.left_msg_tb.text()
		self.bot = _bot.spawn(host, port, botname, ver, login_msg, left_msg, self.uic.chatlog_tb)

		# self.stop_event=threading.Event()
		# self.c_thread = threading.Thread(target=self.log_msg, args=(Log_MSG,))
		# self.c_thread.start()

	# @pyqtSlot(str)
	def log_msg(self,msg):
		while True:
			self.uic.chatlog_tb.setText(msg)

	def chat(self):
		self.bot.chat(self.uic.chat_tb_2.text())

	###	FUNC FOR MAIN PROGRAM	###

	def kickbot(self):
		if BOTLIST != []:
			for BOT in BOTLIST:
				BOT.quit()
				print(f'{BOT.username} has kicked')


if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec())




print('kill')