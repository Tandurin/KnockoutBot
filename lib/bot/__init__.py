from datetime import datetime

from discord.ext.commands import Bot as BotBase
from discord import Embed, File
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

		avatar = self.user.avatar_url
		fileLocationAvatar = "./data/images/profile.png"

		if not self.ready:
			self.ready = True
			self.guild = self.get_guild(435119526200213514)
			print("bot ready")

			channel = self.get_channel(752482031228682340)
			await channel.send("Now online!")

			embed = Embed(title="Now Online!", description="KnockoutBot is now online.", colour=0xFF00A4, timestamp=datetime.utcnow())
			fields = [("Name", "Value", True),
					  ("Another field", "This field is next to the other one.", True),
					  ("A non-inline field", "This field will appear on it's own row.", False)]
			for name, value, inline in fields:
				embed.add_field(name=name, value=value, inline=inline)
			embed.set_author(name="KnockoutBot", icon_url=avatar)
			embed.set_footer(text="This is a footer!")
			embed.set_thumbnail(url=avatar)
			embed.set_image(url=avatar)
			await channel.send(embed=embed)

			await channel.send(file=File(fileLocationAvatar))


		else:
			print("bot reconnected")

	async def on_message(self, message):
		pass

bot = Bot()
