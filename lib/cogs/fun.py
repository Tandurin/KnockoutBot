from random import choice, randint
from typing import Optional

from discord import Member
from discord.ext.commands import Cog
from discord.ext.commands import command

GREETINGS = ['Hey', 'Hello', 'Sup', 'Greetings', 'Hi']
# DICE_ERROR = "I can't roll that many dice. Please try a maximum of 25 dice."


class Fun(Cog):

    def __init__(self, bot):
        self.bot = bot

    @command(name="hello", aliases=["hi"])
    async def say_hello(self, ctx):
        await ctx.send(f"{choice(GREETINGS)} {ctx.author.mention}!")

    # @command(name="dice", aliases=["roll"])
    # async def roll_dice(self, ctx, die_string: str):
    #     dice, value = (int(term) for term in die_string.split("d"))
    #     if dice <= 25:
    #         rolls = [randint(1, value) for i in range(dice)]

    #         await ctx.send(" + ".join([str(r) for r in rolls]) + f" = {sum(rolls)}")

    #     else:
    #         await ctx.send(DICE_ERROR)

    @command(name="slap", aliases=["punch"])
    async def slap_member(self, ctx, member: Member, *,
                          reason: Optional[str] = "for no reason"):
        await ctx.send(f"{ctx.author.display_name} "
                       "slapped {member.mention} {reason}!")

    @command(name="echo", aliases=["say"])
    async def echo_message(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
