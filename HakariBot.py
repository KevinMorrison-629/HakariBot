


import discord
import discord.ext.commands as commands



import multiprocessing

import threading

from itertools import cycle

import typing
import dotenv
import os


from HakariUtils import LogLevel, log
from HakariDatabase import HakariDatabase
from HakariClasses import HakariCommand, CommandsEnum, Metadata



# =============================================================================================== #
#                                          Hakari Bot                                             #
# =============================================================================================== #

class HakariBot(commands.Bot):

    def __init__(self, *args, **kwargs):
        """[INITIALIZER] Default Initializer for discord bot"""
        super().__init__(*args, **kwargs)

        # Used to Store commands incoming for the bot to process
        self.CommandQueue : multiprocessing.Queue[HakariCommand] = multiprocessing.Queue(maxsize=100)
        self.threadPool : multiprocessing.Queue[threading.Thread] = multiprocessing.Queue(maxsize=999)

        # Used to set the bot status (just for a bit of fun i guess)
        self.statusList = cycle([discord.Game('in the Sand'),
                                 discord.Game('with Waifu Bot'),
                                 discord.Game('with myself'),
                                 discord.Activity(type=discord.ActivityType.watching, name='Anime'),
                                 discord.Activity(type=discord.ActivityType.watching, name='you waste your life'),
                                 discord.Activity(type=discord.ActivityType.listening, name='to silence')])
        
        # Start Commands Processesing Threads
        self.__process_command_thread : threading.Thread = threading.Thread(target=self.__process_commands, name="ProcessCommands")
        self.__process_command_thread.start()

        # Used to Store Information about all Characters, Players, Server States
        self.database = HakariDatabase("Hakari.db")

    def __process_commands(self):
        """[Threaded Method] Take the First Command in the Queue and Execute"""
        # TODO : Need to assign multiple threads to work on processing commands

        while True:
            try:
                # Get next command in queue
                comm : HakariCommand = self.CommandQueue.get()
                # Execute Processing on Command
                log(f"Execute Command {comm.command_id} with args [{comm.command_parameters}]", LogLevel.INFO)
            except Exception as exc:
                log(f"Exception When Inserting into Database [{exc}]", LogLevel.ERROR)


    # Initialization Methods
    async def setup_hook(self) -> None:
        """[INITIALIZER] Called when the bot is initialized (before on_ready)"""
        await self.load_extension("CommandsCog")
        return await super().setup_hook()

    # Event Functions
    async def on_guild_join(self, guild : discord.Guild):
        """[EVENT] Called when the bot joins a guild"""
        log(f"Guild Joined [{guild.name}]", LogLevel.INFO)

    async def on_ready(self):
        """[EVENT] Called when the bot is ready to accept commands"""
        log(f'Logged in as {self.user}', LogLevel.INFO)





# =============================================================================================== #
#                                             Main()                                              #
# =============================================================================================== #

if __name__ == "__main__":
    # Load the Bot Secret Token
    dotenv.load_dotenv()
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # Set the Discord Intents (what the bot can do)
    intents = discord.Intents.default()
    intents.message_content = True

    # Initialize the bot
    # Setting "$" as the command prefix for now, may change later to something else
    bot = HakariBot(command_prefix="$", intents=intents)

    # Run the bot
    bot.run(BOT_TOKEN)