import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx): #ping
        message = await ctx.send("ping是...")
        p = round(self.bot.latency*1000)
        await message.edit(content= f"`{p }ms` owo")
        print(f"`{p }ms` owo")
        #round 小數點四捨五入

def setup(bot):
    bot.add_cog(Main(bot))