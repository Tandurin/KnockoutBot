from discord.ext.commands import Cog


class Reactions(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("reactions")

    @Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(f"[RAW] {payload.member.display_name} reacted with {payload.emoji}")

    @Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        member = self.bot.guild.get_member(payload.user_id)
        print(f"[RAW] {member.display_name} removed the reaction of {payload.emoji}")

def setup(bot):
    bot.add_cog(Reactions(bot))