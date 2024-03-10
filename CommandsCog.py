


import discord
import discord.ext.commands as commands
from HakariClasses import HakariCommand, CommandsEnum, Metadata

from HakariUtils import log, LogLevel

from HakariBot import HakariBot

# =============================================================================================== #
#                                             Cogs                                                #
# =============================================================================================== #
    
class CommandsCog(commands.Cog):
    def __init__(self, bot : HakariBot):
        self.bot : HakariBot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")

    @commands.command(name="hello", help="Say Hi!")
    async def hello(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        command = HakariCommand(CommandsEnum.HELLO, [], metadata)
        self.bot.CommandQueue.put(command)
        log(f"Add Command To Queue [{command.command_id}]", LogLevel.INFO)

    @commands.command(name="roll", help="")
    async def roll(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.ROLL, args, metadata)
        self.bot.CommandQueue.put(command)

    @commands.command(name="ct", help="")
    async def coinToss(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.COIN_TOSS, args, metadata)
        self.bot.CommandQueue.put(command)
        return

# Used to Setup the Cogs used in HakariBot
async def setup(bot):
    await bot.add_cog(CommandsCog(bot))