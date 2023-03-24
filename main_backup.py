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

		self.uifunc = UIFunction(self)
		

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


		self.settings = {
		'ip': self.uic.ip_tb.text(),
		'port': self.uic.port_sp.value(),
		'path_name_list': self.uic.name_path_tb.text(),
		'random_name': self.uic.ran_name_cb.isChecked(),
		'version': self.uic.ver_cb.currentText(),
		}
		# self.Bot = Bot()
		# self.Annoying = Annoying()
		self.utility = Utility()

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

	# def JoinLeft(self, stop_event):
	# 	self.settings = {
	# 	'ip': self.uic.ip_tb.text(),
	# 	'port': self.uic.port_sp.value(),
	# 	'path_name_list': self.uic.name_path_tb.text(),
	# 	'random_name': self.uic.ran_name_cb.isChecked(),
	# 	'version': self.uic.ver_cb.currentText(),
	# 	}
	# 	self.STATE = True
	# 	countbot = 1	
	# 	while self.STATE and not stop_event.isSet():
	# 		botuuid = self.utility.GENERATOR_BOT_UUID()
	# 		self.annoyingbot.JoinLeft(self.settings['ip'],
	# 							self.settings['port'],
	# 							botuuid if self.settings['random_name'] else '',
	# 							self.settings['version'],
	# 							self.uic.delay_left_sp.value(),
	# 							0 if self.uic.left_after_login_rb.isChecked() else 1,
	# 							self.uic.botstatus
	# 							)
	# 		time.sleep(self.uic.delay_join1_sp.value())
	# 		self.uic.botcount_lb.setText(f' {countbot}/∞')
	# 		countbot += 1
	# 	self.after_start()

	# def SpamJoin(self, stop_event):
	# 	self.settings = {
	# 	'ip': self.uic.ip_tb.text(),
	# 	'port': self.uic.port_sp.value(),
	# 	'path_name_list': self.uic.name_path_tb.text(),
	# 	'random_name': self.uic.ran_name_cb.isChecked(),
	# 	'version': self.uic.ver_cb.currentText(),
	# 	'max_bot': self.uic.maxbot_sp.value()
	# 	}
	# 	maxbot = self.settings['max_bot']
	# 	countbot = 1
	# 	while maxbot >= countbot and not stop_event.isSet():
	# 		botuuid = self.utility.GENERATOR_BOT_UUID()
		
	# 		bot = self.annoyingbot.SpamJoin(host = self.settings['ip'],
	# 							port = self.settings['port'],
	# 							botname = botuuid if self.settings['random_name'] else '',
	# 							version = self.settings['version'],
	# 							table = self.uic.botstatus)
	# 		BOTLIST.append(bot)
	# 		time.sleep(self.uic.delay_join2_sp.value())
	# 		self.uic.botcount_lb.setText(f' {countbot}/{maxbot}')
	# 		countbot += 1
	# 	self.after_start()

	# def SpamChat(self, stop_event):
	# 	self.settings = {
	# 	'ip': self.uic.ip_tb.text(),
	# 	'port': self.uic.port_sp.value(),
	# 	'path_name_list': self.uic.name_path_tb.text(),
	# 	'random_name': self.uic.ran_name_cb.isChecked(),
	# 	'version': self.uic.ver_cb.currentText(),
	# 	'max_bot2': self.uic.maxbot2_sp.value(),
	# 	}		
	# 	maxbot = self.settings['max_bot2']
	# 	countbot = 1
	# 	while maxbot >= countbot and not stop_event.isSet():
	# 		botuuid = self.utility.GENERATOR_BOT_UUID()
	# 		self.annoyingbot.SpamChat(host = self.settings['ip'],
	# 							port = self.settings['port'],
	# 							botname = botuuid if self.settings['random_name'] else '',
	# 							version = self.settings['version'],
	# 							msg = self.uic.chat_tb.text(),
	# 							delay = self.uic.delay_chat_sp.value(),
	# 							table = self.uic.botstatus
	# 							)
	# 		time.sleep(self.uic.delay_join3_sp.value())
	# 		self.uic.botcount_lb.setText(f' {countbot}/{maxbot}')
	# 		countbot += 1
	# 	self.after_start()
		
	###		END 	###


	def start(self):
		self.uic.ip_tb.setEnabled(False)
		self.uic.port_sp.setEnabled(False)
		self.uic.method_cb.setEnabled(False)
		self.uic.ver_cb.setEnabled(False)
		self.uic.name_path_tb.setEnabled(False)
		self.uic.browse_btn.setEnabled(False)
		self.uic.ran_name_cb.setEnabled(False)
		self.uic.start_btn.setEnabled(False)
		self.uic.start_btn_2.setEnabled(False)
		self.uic.maxbot2_sp.setEnabled(False)
		self.uic.maxbot_sp.setEnabled(False)

		self.uic.stop_btn.setEnabled(True)
		self.uic.stop_btn_2.setEnabled(True)
		self.uic.kick_btn.setEnabled(True)
		self.uic.kick_btn_2.setEnabled(True)

		self.uic.status_lb.setText('On')
		self.uic.status_lb.setStyleSheet('color: rgb(0, 255, 59)')

		if self.uic.method_cb.currentText() == 'JoinLeft':
			self.stop_event=threading.Event()
			self.c_thread = threading.Thread(target=self.JoinLeft, args=(self.stop_event,))
			self.c_thread.start()
		elif self.uic.method_cb.currentText() == 'SpamJoin':
			self.stop_event=threading.Event()
			self.c_thread = threading.Thread(target=self.SpamJoin, args=(self.stop_event,))
			self.c_thread.start()
		elif self.uic.method_cb.currentText() == 'SpamChat':
			self.stop_event=threading.Event()
			self.c_thread = threading.Thread(target=self.SpamChat, args=(self.stop_event,))
			self.c_thread.start()

	def cancel(self):
		self.uic.ip_tb.setEnabled(True)
		self.uic.port_sp.setEnabled(True)
		self.uic.method_cb.setEnabled(True)
		self.uic.ver_cb.setEnabled(True)
		self.uic.name_path_tb.setEnabled(True)
		self.uic.browse_btn.setEnabled(True)
		self.uic.ran_name_cb.setEnabled(True)
		self.uic.start_btn.setEnabled(True)
		self.uic.start_btn_2.setEnabled(True)
		self.uic.maxbot2_sp.setEnabled(True)
		self.uic.maxbot_sp.setEnabled(True)

		self.uic.stop_btn.setEnabled(False)
		self.uic.stop_btn_2.setEnabled(False)
		self.stop_event.set()
		self.display_after_cancel()
		# self.close()

	def after_start(self):
		self.uic.ip_tb.setEnabled(True)
		self.uic.port_sp.setEnabled(True)
		self.uic.method_cb.setEnabled(True)
		self.uic.ver_cb.setEnabled(True)
		self.uic.name_path_tb.setEnabled(True)
		self.uic.browse_btn.setEnabled(True)
		self.uic.ran_name_cb.setEnabled(True)
		self.uic.start_btn.setEnabled(True)
		self.uic.start_btn_2.setEnabled(True)
		self.uic.maxbot2_sp.setEnabled(True)
		self.uic.maxbot_sp.setEnabled(True)

		self.uic.stop_btn.setEnabled(False)
		self.uic.stop_btn_2.setEnabled(False)
		self.uic.status_lb.setText('Off')
		self.uic.status_lb.setStyleSheet('color: rgb(255, 45, 3)')

	def display_after_cancel(self):
		self.uic.status_lb.setText('Off')
		self.uic.status_lb.setStyleSheet('color: rgb(255, 45, 3)')
		self.uic.botcount_lb.setText(f'0/0')

	def kill_proc_tree(self, pid, including_parent=True):    
		parent = psutil.Process(pid)
		if including_parent:
			parent.kill()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec())




print('kill')