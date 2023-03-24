from javascript import require, On
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

		@On(Bot, 'error')
		def error(err, *a):
			print(f"[ERROR] Bot {Bot.username} get error \n{err}")


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
			
# class Bot:
# 	def spawn(self, host, port, botname, ver, login_msg, left_msg, chatlog):
# 		bot = mineflayer.createBot({
# 			'host': host,
# 			'port': port,
# 			'username': botname,
# 			'version': ver,
# 			})

# 		@On(bot, 'login')
# 		def login(this):
# 			bot.chat(login_msg) if login_msg != '' else ''

# 		@On(bot, 'chat')
# 		def _chat(b, _usr, _msg, *a):
# 			print(f'{_usr} >> {_msg}')
# 			__log = chatlog.toPlainText()
# 			Log_MSG = f'{__log}{_usr} >> {_msg}'
# 			# chatlog.setText(f'{__log}{usr} >> {msg}\n')

# 		@On(bot, 'error')
# 		def error(err, *a):
# 			print(err, a)
# 		return bot


# class AnnoyingBot:

# 	def JoinLeft(self, host, port, botname, version, delayleft, lefttype, table):
# 		bot = mineflayer.createBot({
# 		  'host': host,
# 		  'port': port,
# 		  'username': botname,
# 		  'version': version,
# 		})

# 		@On(bot, 'login')
# 		def login(this):
# 			if lefttype == 0:
# 				print(f'NOFITICATION - LOGGED - {botname} has logged in to {host}:{port}')
# 				time.sleep(delayleft)
# 				bot.quit()
# 				print(f"NOFITICATION - QUIT - {botname} has quit.")

# 		@On(bot, "error")
# 		def error(err, *a):
# 			print(f"NOFITICATION - ERROR - {botname}: Connect ERROR")

# 		@On(bot, 'spawn')
# 		def spawn(this):
# 			if lefttype == 1:
# 				print(f'NOFITICATION - LOGGED - {botname} has logged in to {host}:{port}')
# 				time.sleep(delayleft)
# 				bot.quit()
# 				print(f"NOFITICATION - QUIT - {botname} has quit.")

# 	def SpamJoin(self, host, port, botname, version, table):
# 		bot = mineflayer.createBot({
# 		  'host': host,
# 		  'port': port,
# 		  'username': botname,
# 		  'version': version,
# 		})

# 		@On(bot, 'login')
# 		def login(this):
# 			print(f'NOFITICATION - LOGGED - {botname} has logged in to {host}:{port}')
# 			table.insertRow(table.rowCount())
# 			bot = QtWidgets.QTableWidgetItem(botname)
# 			table.setItem(table.rowCount()-1, 0, bot)
# 			status = QtWidgets.QTableWidgetItem("Connected")
# 			table.setItem(table.rowCount()-1, 1, status)

# 		@On(bot, "error")
# 		def error(err, *a):
# 			print(f"NOFITICATION - ERROR - {botname}: Connect ERROR")
# 		return bot

# 	def SpamChat(self, host, port, botname, version, msg, delay, table):
# 		bot = mineflayer.createBot({
# 		  'host': host,
# 		  'port': port,
# 		  'username': botname,
# 		  'version': version,
# 		})

# 		@On(bot, 'login')
# 		def login(this):
# 			print(f'NOFITICATION - LOGGED - {botname} has logged in to {host}:{port}')
# 			table.insertRow(table.rowCount())
# 			bot = QtWidgets.QTableWidgetItem(botname)
# 			table.setItem(table.rowCount()-1, 0, bot)
# 			status = QtWidgets.QTableWidgetItem("Connected")
# 			table.setItem(table.rowCount()-1, 1, status)

# 		@On(bot, 'spawn')
# 		def spawn(this):
# 			bot.chat(msg)
# 			time.sleep(delay)

# 		@On(bot, "error")
# 		def error(err, *a):
# 			print(f"NOFITICATION - ERROR - {botname}: Connect ERROR")