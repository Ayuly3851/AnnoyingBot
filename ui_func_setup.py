# -*- coding: utf-8 -*-

# SETUP FUNCTION FOR THE UI

from PyQt5 import (QtCore, QtGui, QtWidgets)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 

from ui_draw import Ui_MainWindow
from ui_function import UIFunction
from Utility import SideGrip
## CLEAR CONSOLE ##
__import__('os').system('cls')

class Ui_Function(object):
	def setupUiFunction(self, MainWindow):
		## HIDE TITLE BAR ##
		MainWindow.setWindowFlag(Qt.FramelessWindowHint)
		## SETUP GRIP ##
		MainWindow.sideGrips = [
			SideGrip(MainWindow, QtCore.Qt.LeftEdge),
			SideGrip(MainWindow, QtCore.Qt.TopEdge), 
			SideGrip(MainWindow, QtCore.Qt.RightEdge), 
			SideGrip(MainWindow, QtCore.Qt.BottomEdge), 
		]
		MainWindow.cornerGrips = [QtWidgets.QSizeGrip(MainWindow) for i in range(4)]
		## GRIPSIZE ##
		MainWindow._gripSize = 2

		## LOAD GUI ##
		MainWindow.uic = Ui_MainWindow()
		## SETUP GUI ##
		MainWindow.uic.setupUi(MainWindow)

		## LOAD FUNCTION ##
		MainWindow.uifunc = UIFunction(MainWindow)
		## SET UI WHEN UI LOADED ##
		MainWindow.uifunc.SetUiLoaded()

	## GRIP RESIZE WINDOW ##
	@property
	def gripSize(self, MainWindow):
		return MainWindow._gripSize

	def setGripSize(self, MainWindow, size):
		if size == MainWindow._gripSize:
			return
		MainWindow._gripSize = max(2, size)
		MainWindow.updateGrips()

	def updateGrips(self, MainWindow):
		MainWindow.setContentsMargins(*[MainWindow.gripSize] * 4)
		outRect = MainWindow.rect()
		inRect = outRect.adjusted(MainWindow.gripSize, MainWindow.gripSize,
			-MainWindow.gripSize, -MainWindow.gripSize)
		MainWindow.cornerGrips[0].setGeometry(
			QtCore.QRect(outRect.topLeft(), inRect.topLeft()))
		MainWindow.cornerGrips[1].setGeometry(
			QtCore.QRect(outRect.topRight(), inRect.topRight()).normalized())
		MainWindow.cornerGrips[2].setGeometry(
			QtCore.QRect(inRect.bottomRight(), outRect.bottomRight()))
		MainWindow.cornerGrips[3].setGeometry(
			QtCore.QRect(outRect.bottomLeft(), inRect.bottomLeft()).normalized())

		MainWindow.sideGrips[0].setGeometry(
			0, inRect.top(), MainWindow.gripSize, inRect.height())
		MainWindow.sideGrips[1].setGeometry(
			inRect.left(), 0, inRect.width(), MainWindow.gripSize)
		MainWindow.sideGrips[2].setGeometry(
			inRect.left() + inRect.width(), 
			inRect.top(), MainWindow.gripSize, inRect.height())
		MainWindow.sideGrips[3].setGeometry(
			MainWindow.gripSize, inRect.top() + inRect.height(), 
			inRect.width(), MainWindow.gripSize)

	def resizeEvent(self, MainWindow, event):
		QtWidgets.QMainWindow.resizeEvent(MainWindow, event)
		MainWindow.updateGrips()

	## MOVE WINDOW ##
	def mousePressEvent(self, MainWindow, event):
		MainWindow.oldPos = event.globalPos()

	def mouseMoveEvent(self, MainWindow, event):
		delta = QPoint (event.globalPos() - MainWindow.oldPos)
		MainWindow.move(MainWindow.x() + delta.x(), MainWindow.y() + delta.y())
		MainWindow.oldPos = event.globalPos()