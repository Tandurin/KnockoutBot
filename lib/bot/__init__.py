from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = "+"
OWNER_IDS = [210003268082991104]

class Bot(BotBase):
	def __init__(self):
		self.PREFIX = PREFIX
		self.ready = False
		self.guild = None
		self.scheduler = AsyncIOScheduler()

		super().__init__(command_prefix=PREFIX, owners_ids=OWNER_IDS)

	def run(self, version):
		self.VERSION = version

		with open("./lib/bot/token", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read()

		print("running bot...")
		super().run(self.TOKEN, reconnect=True)

	async def on_connect(self):
		print("Bot Connected")

	async def on_disconnect(self):
		print("Bot Disconnected")

	async def on_ready(self):
		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(435119526200213514)
			print("bot ready")

		else:
			print("bot reconnected")

	async def on_message(self, message):
		pass

bot = Bot()
