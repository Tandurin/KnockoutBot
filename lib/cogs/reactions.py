from discord.ext.commands import Cog
from discord.ext import commands
from discord import Member
from discord.utils import get
from discord import Guild


class Reactions(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("reactions")


    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(f"[RAW] {payload.member.display_name} reacted with {payload.emoji.name}")
        if payload.emoji.name == "KO_":
            #Do code

            msg = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            member = msg.author
            role_name = "Knockout"
            members = Guild.members
            for m in members:
                try:
                    await member.remove_roles(role_name)
                except:
                    print(f"Couldn't remove roles from {m}")        
            print(f"Somebody needs to be knocked out!")

            await payload.member.add_roles("Knockout")
        else:
            pass

    @Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        member = self.bot.guild.get_member(payload.user_id)
        pass

def setup(bot):
    bot.add_cog(Reactions(bot))