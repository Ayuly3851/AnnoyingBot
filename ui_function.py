# -*- coding: utf-8 -*-

# FUNCTION FOR UI

import Core, threading
from PyQt5 import (QtCore, QtGui, QtWidgets)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

class UIFunction:

	def __init__(self, Window):
		self.Annoying = Core.Annoying()
		self.Bot = Core.Bot()
		self.Window = Window

	## CLOSE THE WINDOW ##
	def CloseWindow(self,):
		self.Window.close()

	## CHANGE THE STACKEDWIDGET INDEX ##
	def ChangeStackedWidget(self, StackedWidget, Index):
		StackedWidget.setCurrentIndex(Index)

	def SetUiLoaded(self,):
		## CONTROL BUTTON ##
		self.Window.uic.close_btn.clicked.connect(lambda: self.CloseWindow())
		self.Window.uic.max_btn.clicked.connect(lambda: self.Window.showMaximized())
		self.Window.uic.mini_btn.clicked.connect(lambda: self.Window.showMinimized())
		## HIDE UP, DOWN ARROW FROM SPINBOX ##
		self.Window.uic.port_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.port_sp_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.delay_join1_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.delay_left_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.maxbot_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.maxbot2_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.delay_join2_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.delay_chat_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		self.Window.uic.delay_join3_sp.setButtonSymbols(QAbstractSpinBox.NoButtons)
		## CONNECT BUTTON TO FUNCTION ##
		self.Window.uic.main_btn.clicked.connect(lambda: self.ChangeStackedWidget(self.Window.uic.stackedWidget, 0))
		self.Window.uic.joinleft_btn.clicked.connect(lambda: self.ChangeStackedWidget(self.Window.uic.stackedWidget, 1))
		self.Window.uic.spamjoin_btn.clicked.connect(lambda: self.ChangeStackedWidget(self.Window.uic.stackedWidget, 2))
		self.Window.uic.spamchat_btn.clicked.connect(lambda: self.ChangeStackedWidget(self.Window.uic.stackedWidget, 3))
		self.Window.uic.botcontrol_btn.clicked.connect(lambda: self.ChangeStackedWidget(self.Window.uic.stackedWidget, 4))
		self.Window.uic.start_btn.clicked.connect(lambda: self.Start())
		self.Window.uic.start_btn_2.clicked.connect(lambda: self.Start())
		self.Window.uic.stop_btn.clicked.connect(lambda: self.Stop())
		self.Window.uic.stop_btn_2.clicked.connect(lambda: self.Stop())
		# self.Window.uic.spawn_btn.clicked.connect(self.Window.spawnbot)
		# self.Window.uic.chat_btn.clicked.connect(self.Window.chat)

		## DISABLE BUTTON ##
		self.Window.uic.stop_btn.setEnabled(False)
		self.Window.uic.stop_btn_2.setEnabled(False)
		self.Window.uic.quit_btn.setEnabled(False)
		## SET STATUS ##
		self.Window.uic.status_lb.setText('Off')
		self.Window.uic.status_lb.setStyleSheet('color: rgb(255, 45, 3)')

	## START ANNOYING BOT ##
	def Start(self,):
		if self.Window.uic.method_cb.currentIndex() == 0:
			self.DelayLogin = self.Window.uic.delay_join1_sp.value()
		elif self.Window.uic.method_cb.currentIndex() == 1:
			self.DelayLogin = self.Window.uic.delay_join2_sp.value()
		else:
			self.DelayLogin = self.Window.uic.delay_join3_sp.value()

		## GET CONFIG ##
		self.config = {
			'host': self.Window.uic.ip_tb.text(),
			'port': self.Window.uic.port_sp.value(),
			'version': self.Window.uic.ver_cb.currentText(),
			'type': self.Window.uic.method_cb.currentIndex() + 1,
			'delaylogin': self.DelayLogin,
			'delayleft': self.Window.uic.delay_left_sp.value(),
			'lefttype': 0 if self.Window.uic.left_after_login_rb.isChecked() else 1,
			'delaychat': self.Window.uic.delay_chat_sp.value(),
			'chatmessage': self.Window.uic.chat_tb.text(),
			'table': self.Window.uic.botstatus,
		}
		## SET UI ##
		self.SetUi(True)
		## SET CONFIG FOR ANNOYING ##
		self.Annoying.SetConfig(self.config)
		## GET METHOD ##
		self.method = self.Window.uic.method_cb.currentIndex() + 1
		## START ANNOYING ##
		if self.method == 1:
			self.stop_event=threading.Event()
			self.c_thread = threading.Thread(target=self.Annoying.JoinLeft, args=(self.Window, self.stop_event,))
			self.c_thread.start()
		elif self.method == 2:
			self.stop_event=threading.Event()
			self.c_thread = threading.Thread(target=self.Annoying.SpamBot, args=(self.Window, self.stop_event, self.Window.uic.maxbot_sp.value(),))
			self.c_thread.start()
		elif self.method == 3:
			self.stop_event=threading.Event()
			self.c_thread = threading.Thread(target=self.Annoying.SpamChat, args=(self.Window, self.stop_event, self.Window.uic.maxbot2_sp.value(),))
			self.c_thread.start()

	## STOP ANNOYING BOT ##
	def Stop(self,):
		self.SetUi(False)
		self.KickBot()
		self.stop_event.set()

	## KICK BOT IN SERVER ##
	def KickBot(self,):
		self.Annoying.KickBot(self.Window.uic.method_cb.currentIndex() + 1)

	## SET UI WHEN START OR STOP BUTTON CLICKED ##
	def SetUi(self, _bool):
		self.Window.uic.ip_tb.setEnabled(not _bool)
		self.Window.uic.port_sp.setEnabled(not _bool)
		self.Window.uic.method_cb.setEnabled(not _bool)
		self.Window.uic.ver_cb.setEnabled(not _bool)
		self.Window.uic.name_path_tb.setEnabled(not _bool)
		self.Window.uic.browse_btn.setEnabled(not _bool)
		self.Window.uic.ran_name_cb.setEnabled(not _bool)
		self.Window.uic.start_btn.setEnabled(not _bool)
		self.Window.uic.start_btn_2.setEnabled(not _bool)
		self.Window.uic.maxbot2_sp.setEnabled(not _bool)
		self.Window.uic.maxbot_sp.setEnabled(not _bool)

		self.Window.uic.stop_btn.setEnabled(_bool)
		self.Window.uic.stop_btn_2.setEnabled(_bool)

		self.Window.uic.status_lb.setText('On') if _bool else self.Window.uic.status_lb.setText('Off')
		self.Window.uic.status_lb.setStyleSheet('color: rgb(0, 255, 59)') if _bool else self.Window.uic.status_lb.setStyleSheet('color: rgb(255, 45, 3)')

