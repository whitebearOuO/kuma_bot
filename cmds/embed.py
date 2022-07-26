import discord
from discord.ext import commands
from core.classes import Cog_Extension
import time
import datetime

class Embed(Cog_Extension):

    @commands.command()
    async def info(self, ctx): #info 詳細資訊
        username = ctx.message.author.name
        await ctx.send(username)
        embed=discord.Embed(title="kuma", url="https://discord.com/api/oauth2/authorize?client_id=708881902135672884&permissions=522304&scope=bot", description="一個測試中的bot owo", color=0x37e1dd, timestamp=datetime.datetime.today())
        embed.set_author(name="白熊", url="https://whitebearouob.blogspot.com/", icon_url="https://1.bp.blogspot.com/-73sa6KNYNEw/XXSaqPkzW9I/AAAAAAAABPE/FQkgJuHgfyceHMON48eMDy8GLkMv9LeMQCLcBGAs/s1600/1518182898346.png")
        embed.set_thumbnail(url="https://images6.alphacoders.com/674/674742.jpg")
        embed.add_field(name="入侵幾個伺服器了owo", value=f"{len(self.bot.guilds)}")
        embed.add_field(name="可...可惡", value="bot好難寫owo", inline=False)
        await ctx.send(embed=embed)
        print("已送出info")

def setup(bot):
    bot.add_cog(Embed(bot))