# -*- coding: utf-8 -*-

# CORE FOR ANNOYINGBOT

from javascript import require, On, Once, AsyncTask, once, off
mineflayer = require('mineflayer')
from time import sleep
from Utility import Utility

"""
BotType:
	0 == Normal Bot
	1 == JoinLeft
	2 == SpamJoin
	3 == SpamChat
"""

class Bot:
	def __init__(self):
		self.OffEventListener = False
		self.log_chat = ""

		self.BotJoinSpamList = []
		self.BotChatSpamList = []
		self.BotNormalList = []

	def SetConfig(self, config):
		self.Host = config['host']
		self.Port = config['port']
		self.Version = config['version']
		self.BotType = config['type']
		self.DelayLogin = config['delaylogin']
		self.DelayLeft = config['delayleft']
		self.LeftType = config['lefttype']
		self.ChatMessage = config['chatmessage']
		self.DelayChat = config['delaychat']
		self.Table = config['table']

	def SetBotName(self, botname):
		self.BotName = botname

	def Spawn(self):
		Bot = mineflayer.createBot({
			'host': self.Host,
			'port': self.Port,
			'username': self.BotName,
			'version': self.Version,
		})

		self.BotNormalList.append(Bot) if self.BotType == 0 else None
		self.BotJoinSpamList.append(Bot) if self.BotType == 2 else None
		self.BotChatSpamList.append(Bot) if self.BotType == 3 else None

		@On(Bot, 'login')
		def login(this):
			sleep(self.DelayLeft) if self.BotType == 1 and self.LeftType == 0 else None
			Bot.quit() if self.BotType == 1 and self.LeftType == 0 else None

		@On(Bot, 'spawn')
		def spawn(this):
			sleep(self.DelayLeft) if self.BotType == 1 and self.LeftType == 1 else None
			Bot.quit() if self.BotType == 1 and self.LeftType == 1 else None
			def KillAura():
				print(Bot.entities)
			KillAura() if self.BotType == 2 else None

		@On(Bot, 'chat')
		def logger_chat(this, sender, message, *a):
			self.log_chat = self.log_chat + f"{sender} >> {message}\n" if self.BotType == 0 else None

		@On(Bot, 'error')
		def error(err, *a):
			print(f"[ERROR] Bot {Bot.username} get error \n{err}")

		if self.OffEventListener:
			off(Bot, 'login', login)
			off(Bot, 'spawn', spawn)
			off(Bot, 'chat', logger_chat)
			off(Bot, 'error', error)

class Annoying:
	def _init_(self,):
		self.config = {
			'host': self.Host,
			'port': self.Port,
			'version': self.Version,
			'type': self.BotType,
			'delaylogin': self.DelayLogin,
			'delayleft': self.DelayLeft,
			'lefttype': self.LeftType,
			'delaychat': self.DelayChat,
			'chatmessage': self.ChatMessage,
			'table': self.Table,
		}
		self.Bot = Bot()
		self.Bot.SetConfig(self.config)

		self.Utility = Utility()
	
	def SetConfig(self, config):
		self.Host = config['host']
		self.Port = config['port']
		self.Version = config['version']
		self.BotType = config['type']
		self.DelayLogin = config['delaylogin']
		self.DelayLeft = config['delayleft']
		self.LeftType = config['lefttype']
		self.ChatMessage = config['chatmessage']
		self.DelayChat = config['delaychat']
		self.Table = config['table']
		self._init_()

	def JoinLeft(self, Window, stop_event):
		AmountBot = 1
		while True and not stop_event.isSet():
			BotName = self.Utility.GENERATOR_BOT_UUID()
			self.Bot.SetBotName(BotName)
			self.Bot.Spawn()
			sleep(self.DelayLogin)
			Window.uic.botcount_lb.setText(f' {AmountBot} / ∞')
			AmountBot += 1

	def SpamChat(self, Window, stop_event, MaxBot):
		AmountBot = 1
		while MaxBot >= AmountBot and not stop_event.isSet():
			BotName = self.Utility.GENERATOR_BOT_UUID()
			self.Bot.SetBotName(BotName)
			self.Bot.Spawn()
			sleep(self.DelayLogin)
			Window.uic.botcount_lb.setText(f' {AmountBot} / {MaxBot}')
			AmountBot += 1
		# SPAWN DONE, SPAM CHAT
		while True and not stop_event.isSet():
			for bot in self.Bot.BotChatSpamList:
				sleep(self.DelayChat)
				bot.chat(self.ChatMessage)

	def SpamBot(self, Window, stop_event, MaxBot):
		AmountBot = 1
		while MaxBot >= AmountBot and not stop_event.isSet():
			BotName = self.Utility.GENERATOR_BOT_UUID()
			self.Bot.SetBotName(BotName)
			self.Bot.Spawn()
			sleep(self.DelayLogin)
			Window.uic.botcount_lb.setText(f' {AmountBot} / {MaxBot}')
			AmountBot += 1

	def KickBot(self, Type, Username = None):
		if Type == 0:
			for Bot in self.BotNormalList:
				if Bot.username == Username:
					Bot.quit()
		elif Type == 2:
			for Bot in self.BotJoinSpamList:
				Bot.quit()
		elif Type == 3:
			for Bot in self.BotChatSpamList:
				Bot.quit()
