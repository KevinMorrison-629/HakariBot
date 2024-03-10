


from HakariBot import HakariBot
from HakariClasses import HakariCommand, CommandsEnum, Metadata, Character, Series

from HakariUtils import log, LogLevel

from Games import CoinTossGame

import discord



class CharEmbed(discord.Embed):
    def __init__(self, char : Character):
        super(CharEmbed, self).__init__()
        self.title : str = char.name
        self.type : str = "rich"
        self.description : str = char.series
        self.color = discord.Color.dark_red()
        self.set_image(url=f"https://kevinmorrison-629.github.io/HakariBot/images/{char.image_urls[0]}")



class CommandsExecutor:
    def __init__(self, bot : HakariBot):
        self.bot : HakariBot = bot

    async def Execute(self, command : HakariCommand):
        match command.command_id:
            case CommandsEnum.SEARCH:
                log("Search", LogLevel.DEBUG)
                name = " ".join(command.command_parameters[1:])
                ec, char = self.bot.database.GetCharacterWithName(name)
                
                if (ec.ec):
                    # Get the Channel that the command was sent in
                    chan = await self.bot.fetch_channel(command.metadata.channel_id)

                    # Create a Message Object with the character card requested
                    embed = CharEmbed(char)
                    await chan.send(content="", embed=embed)
                else:
                    log(f"Could Not Get Character with Name [{name}] [{ec}]")