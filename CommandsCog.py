


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
        log(f"Ready!", LogLevel.INFO)

    # TODO : Need to rename the commands such that they dont conflict with Mudae (since we probably want both bots in the server)

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
    
    @commands.command(name="rps", help="")
    async def rockPaperScissors(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.ROCK_PAPER_SCISSORS, args, metadata)
        self.bot.CommandQueue.put(command)

    @commands.command(name="allowance", help="")
    async def allowance(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.DAILY_ALLOWANCE, args, metadata)
        self.bot.CommandQueue.put(command)

    @commands.command(name="top", help="")
    async def top(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.TOP_CHARACTERS, args, metadata)
        self.bot.CommandQueue.put(command)

    @commands.command(name="team", help="")
    async def team(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.OWNED_CHARACTERS, args, metadata)
        self.bot.CommandQueue.put(command)

    @commands.command(name="divorce", help="")
    async def divorce(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.DIVORCE, args, metadata)
        self.bot.CommandQueue.put(command)

    @commands.command(name="search", help="")
    async def search(self, ctx : commands.Context):
        metadata = Metadata(ctx.author.id, ctx.channel.id, ctx.guild.id)
        args = ctx.message.content.split()
        command = HakariCommand(CommandsEnum.SEARCH, args, metadata)
        self.bot.CommandQueue.put(command)

# Used to Setup the Cogs used in HakariBot
async def setup(bot : HakariBot):
    await bot.add_cog(CommandsCog(bot))