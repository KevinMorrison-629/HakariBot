





import discord
from discord.ext import commands

import random







class CoinTossGame:
    def __init__(self, ctx : commands.Context, userid : int, gameid):
        
        self.userid = userid
        # Embed
        self.embed : discord.Embed = discord.Embed(title="Coin Toss",
                                   type="rich",
                                   description="Chance You're Luck!",
                                   color=discord.Color.gold())
        self.embed.set_image(url=f"https://kevinmorrison-629.github.io/HakariBot/gif/coinflip_gif.gif")
        self.id : int = gameid
        # Button
        self.button : discord.ui.Button = discord.ui.Button(style=discord.ButtonStyle.gray,
                                                            label="flip",
                                                            custom_id=str(self.id))
        self.button.callback = self.callback
        self.view = discord.ui.View()
        self.view.add_item(self.button)
        self.view.timeout = 30
        self.message = self.startCoinToss(ctx)

    def getUserOdds(self) -> float:
        return 0.5
    def getResults(self) -> bool:
        return random.random() <= self.getUserOdds()

    # Methods
    async def callback(self, interaction : discord.Interaction):
        if interaction.user.id == self.userid:
            self.embed.set_image(url=f"https://kevinmorrison-629.github.io/HakariBot/gif/coinflip_jpg.jpg")
            if self.getResults():
                self.embed.description = "You Won!"
                print("You Won!")
            else:
                self.embed.description = "You Lost. . ."
                print("You Lost. . .")
            await interaction.message.edit(embed=self.embed)
        self.view.remove_item(self.button)
        self.view.stop()
            
    async def startCoinToss(self, ctx : commands.Context) -> None:
        return await ctx.send(embed=self.embed, view=self.view)