# Declare Imports

from datetime import datetime

from discord.ext.commands import Bot as BotBase
from discord import Embed, File
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Declare Global Vars
PREFIX = "+"
OWNER_IDS = [210003268082991104]


# Define basic operation class
class Bot(BotBase):

    def __init__(self):
        # Declare local method variables
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

# Super __init__ as class copy
        super().__init__(command_prefix=PREFIX, owners_ids=OWNER_IDS)

# Boot function
    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Booting up KnockoutBot")
        super().run(self.TOKEN, reconnect=True)

    # Connected function
    async def on_connect(self):
        print("Bot Connected")

    # Disconnected function
    async def on_disconnect(self):
        print("Bot Disconnected")

#	async def on_error(self, err, *args, **kwargs):
#		if err == "on_command_error":
#			await args[0].send("Something went wrong.")
#
#		raise

    # Bot connected to server
    async def on_ready(self):

        # Define local method variables
        avatar = self.user.avatar_url
        fileLocationAvatar = "./data/images/profile.png"
        baseColour = 0xFF00A4

        if not self.ready:
            # Set connected state
            self.ready = True
            self.guild = self.get_guild(435119526200213514)
            print("Bot Ready For Operation")

            # Set Command-dump channel
            channel = self.get_channel(752482031228682340)
            await channel.send("Now online!")

            embed = Embed(title="Now Online!",
                          description="KnockoutBot is now online.",
                          colour=baseColour, timestamp=datetime.utcnow())
            fields = [("Name", "Value", True),
                      ("Another field", "This field is next to the other one.",
                       True),
                      ("A non-inline field",
                       "This field will appear on it's own row.", False)]
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

    # Check for message || Currently unused
    async def on_message(self, message):
        pass


bot = Bot()
