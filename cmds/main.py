import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self, ctx): #ping
        message = await ctx.send("ping是...")
        p = round(self.bot.latency*1000)
        await message.edit(content= f"`{p }ms` owo")
        print(f"`{p }ms` owo")
        #round 小數點四捨五入

    @commands.command()
    async def hi(self,ctx):
        await ctx.send("1234")

def setup(bot):
    bot.add_cog(Main(bot))