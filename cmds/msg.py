import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Msg(Cog_Extension):
   @commands.Cog.listener()
   async def on_message(self,msg):

        if "362261823040389123" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("拜託你們，先幫ㄅㄒ撐個10秒左右就好")

        elif msg.content.endswith("owo") and msg.author != self.bot.user:
            await msg.channel.send("你也是owo教的嗎")

        elif "z_sui_yada" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/emojis/882566781011644427.gif?size=96&quality=lossless")
        
        elif "sui啦" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://media.discordapp.net/attachments/528777088392757260/904307841861566484/picture_suila_0614.jpg")
        
        elif msg.content.endswith("的機率") and msg.author != self.bot.user and "星爆" in msg.content:
            await msg.channel.send("48763%")
        
        elif msg.content.endswith("的機率") and len(msg.content)>3 and msg.author != self.bot.user:
            a=(random.randint(0,100))
            a=str(a)
            b=(a+"%")
            await msg.channel.send(b)
        
        elif "星爆" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904369881691074560/f8c2c3e8af3782606fd163b8ff6eb4e6.gif")
        
        elif "噓" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("勇者削弱了 1 點精神")
        
        elif "好了ㄝ" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("又好了ㄝ 到底")
        
        elif "騙人" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://media.discordapp.net/attachments/711411107738288160/904376682838892554/47eb58a327c095b5a80512e8e4720bf3.png?width=801&height=450")
        
        elif "戲劇化" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904376938750152704/EPGQobk.png")
        
        elif "你怎麼可以這樣" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904377414778507264/85445f5013f1572f2c208ea3000509f1.png")
        
        elif "好色喔" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904370301893230592/4fd0c420-1c3c-11ec-b1ff-ea1868351416.png")
        
        elif "好電" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/emojis/855433255871447051.gif?size=96")
        
        elif "電神" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/emojis/855433255871447051.gif?size=96")
        
        elif "教嗎" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("教嗎")
        
        elif "好耶" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904377925451800626/latest.png")
        
        elif "菜B8" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914464579352920116/2ddcfb8d83fc6420155791b887806ec9.png")
        
        elif "幹你娘" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914465368360222740/b88f705a275bcacca1044735f7d89035.png")
        
        elif "stay cool" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914465989289189386/66e047c5ee25f1afd236f873ea4fa55e.png")
        
        elif "通知" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914466160437788712/79b73668adb519bc672961345add65e0.png")
        
        elif "更快" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914466472624025650/efb1da15cf66f0a35f46184d3eac1d37.png")
        
        elif "結束" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("https://cdn.discordapp.com/attachments/902205400538034316/917260438268436520/9711f426f96d75947882122126dd0412.png")
        
        await self.bot.process_commands(msg)
        #if msg.contect in keyword and   

def setup(bot):
    bot.add_cog(Msg(bot))