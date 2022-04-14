import discord
from discord.ext import commands
import requests,os,urllib
import time
import json
import random
from time import sleep
import datetime
import keep_alive

'''======================================================================================='''

with open('setting.json', 'r', encoding='utf8') as jfile:
	jdata = json.load(jfile)

'''======================================================================================='''

bot = commands.Bot(command_prefix='owo ') #呼叫bot的方法 owo

#event區

@bot.event #這裡的會在小黑窗出來
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Minecraft 111學年度先行版學習歷程更新"))
    print('logging as') 
    print(bot.user.name) #bot的名字 kuma
    print(bot.user.id) #bot的id 70啥的
    print('------')

@bot.event
async def on_member_join(member):
	print(f'{member} join!')
	channel = bot.get_channel(int(jdata['Welcome_channel']))
	await channel.send(f'{member} join! :tada::tada::tada:')

@bot.event
async def on_member_remove(member):
	print(f'{member} leave!')
	channel = bot.get_channel(int(jdata['Leave_channel']))
	await channel.send(f'{member} leave!:disappointed_relieved:')

@bot.event
async def on_message(msg):
    if "owo" in msg.content and msg.author != bot.user:
        await msg.channel.send("owo")
    elif msg.content.endswith("modo hayaku"):
        await msg.channel.send("還要更慢")
    elif msg.content.endswith("owo") and msg.author != bot.user:
        await msg.channel.send("你也是owo教的嗎")
    elif "sui啦" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://media.discordapp.net/attachments/528777088392757260/904307841861566484/picture_suila_0614.jpg")
    elif msg.content.endswith("的機率") and msg.author != bot.user and "星爆" in msg.content:
        await msg.channel.send("48763%")
    elif msg.content.endswith("的機率") and len(msg.content)>3 and msg.author != bot.user:
        a=(random.randint(0,100))
        a=str(a)
        b=(a+"%")
        await msg.channel.send(b)
    elif "星爆" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904369881691074560/f8c2c3e8af3782606fd163b8ff6eb4e6.gif")
    elif "噓" in msg.content and msg.author != bot.user:
        await msg.channel.send("勇者削弱了 1 點精神")
    elif "騙人" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://media.discordapp.net/attachments/711411107738288160/904376682838892554/47eb58a327c095b5a80512e8e4720bf3.png?width=801&height=450")
    elif "戲劇化" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904376938750152704/EPGQobk.png")
    elif "你怎麼可以這樣" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904377414778507264/85445f5013f1572f2c208ea3000509f1.png")
    elif "好色喔" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904370301893230592/4fd0c420-1c3c-11ec-b1ff-ea1868351416.png")
    elif "好電" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/emojis/855433255871447051.gif?size=96")
    elif "電神" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/emojis/855433255871447051.gif?size=96")
    elif "教嗎" in msg.content and msg.author != bot.user:
        await msg.channel.send("教嗎")
    elif "好耶" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/904377925451800626/latest.png")
    elif "菜B8" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914464579352920116/2ddcfb8d83fc6420155791b887806ec9.png")
    elif "幹你娘" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914465368360222740/b88f705a275bcacca1044735f7d89035.png")
    elif "好吧" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914465821827407892/RBoqkhk.png")
    elif "stay cool" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914465989289189386/66e047c5ee25f1afd236f873ea4fa55e.png")
    elif "通知" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914466160437788712/79b73668adb519bc672961345add65e0.png")
    elif "更快" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/711411107738288160/914466472624025650/efb1da15cf66f0a35f46184d3eac1d37.png")
    elif "結束" in msg.content and msg.author != bot.user:
        await msg.channel.send("https://cdn.discordapp.com/attachments/902205400538034316/917260438268436520/9711f426f96d75947882122126dd0412.png")
    await bot.process_commands(msg)
    #if msg.contect in keyword and 

@bot.event #成員狀態改變
async def on_member_update(before, after):
    if str(before.status) != str(after.status):
        print(f"{after.name} 現在ㄉ狀態是 {after.status}")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

'''======================================================================================='''
       
@bot.command()
async def add_diary(ctx, title, date,* , content): #增加日記
    with open("diary/"+title, 'w') as f:
        print(date, content, sep= '\n', file = f)
    await ctx.send('done')
    print("日記增加完成owo")
    
@bot.command()
async def view(ctx, which, info): #查看日記
    if which == 'date':
        files = os.listdir("diary")
        for i in files:
            path = "diary/"+i
            s = open(path, 'r').read()
            title = s.split('\n')[0]
            if title == info:
                await ctx.send(s)
    elif which == 'which':
        files = os.listdir("diary")
        if info in files:
            #s = open("diary/"+info, 'r').read()
            f = open("diary/"+info, 'r')
            s = f.read()
            f.close()
            await ctx.send(s)
    print("成功查看日記owo")
    
'''======================================================================================='''

@bot.command()
async def info(ctx): #詳細資訊 但其實不怎麼詳細
    username = ctx.message.author.name
    await ctx.send(username)
    embed=discord.Embed(title="kuma", url="https://discord.com/api/oauth2/authorize?client_id=708881902135672884&permissions=522304&scope=bot", description="一個測試中的bot owo", color=0x37e1dd, timestamp=datetime.datetime.today())
    embed.set_author(name="白熊", url="https://whitebearouob.blogspot.com/", icon_url="https://1.bp.blogspot.com/-73sa6KNYNEw/XXSaqPkzW9I/AAAAAAAABPE/FQkgJuHgfyceHMON48eMDy8GLkMv9LeMQCLcBGAs/s1600/1518182898346.png")
    embed.set_thumbnail(url="https://images6.alphacoders.com/674/674742.jpg")
    embed.add_field(name="入侵幾個伺服器了owo", value=f"{len(bot.guilds)}")
    embed.add_field(name="可...可惡", value="bot好難寫owo", inline=False)
    await ctx.send(embed=embed)
    print("已送出info owo")
    
bot.remove_command('help') #刪除原本的help

@bot.command()
async def help(ctx): #我自己的help OuO
    embed=discord.Embed(title="那個神奇的help選單OuO", description="所有的指令開頭都是owo喔", color=0x37e1dd, timestamp=datetime.datetime.now())
    embed.set_thumbnail(url="https://images6.alphacoders.com/674/674742.jpg")
    embed.add_field(name="owo help", value="跳出help清單", inline=False) #1
    embed.add_field(name="owo info", value="有關bot的資訊", inline=False) #2
    embed.add_field(name="owo ping", value="眾所皆知的ping就不用解釋ㄌㄅ", inline=False) #3
    embed.add_field(name="owo fox", value="狐狸照片精選", inline=False) #4
    embed.add_field(name="owo clean", value="刪除訊息", inline=False) #5
    embed.add_field(name="owo say [訊息]", value="bot幫你說話，偷嘴人的好工具", inline=False) #6
    embed.add_field(name="以下指令暫時無法使用", value="待修復", inline=False)
    embed.add_field(name="owo add_diary [title] [date] [content] ", value="紀錄日記(標題不可有空白，內容可以)", inline=False)
    embed.add_field(name="owo view title [title]", value="以標題去搜尋日記", inline=False)
    embed.add_field(name="owo view date [date]", value="以日期去搜尋日記", inline=False)
    embed.add_field(name="owo upload [tag] [date]", value="上傳圖片", inline=False)
    embed.add_field(name="owo search_pic [tag/date]", value="搜尋上傳的圖片", inline=False)
    embed.set_footer(text="指令持續增加中owo")
    await ctx.send(embed=embed)
    print("已送出help列表owo")

@bot.command()
async def upload(ctx, tag, date):
    response = requests.get(ctx.message.attachments[0].url)
    file = open("picture/"+tag+" "+date+".jpg", "wb")
    file.write(response.content)
    file.close()
    await ctx.send("圖片儲存完成owo")
    print("圖片已儲存")

@bot.command()
async def search_pic(ctx, info):
    files = os.listdir("picture")
    for i in files:
        tmp = i.split()
        if info == tmp[0] or info+".jpg" == tmp[1]:
            with open("picture/"+i, 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file = picture)

@bot.command() #複誦訊息
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command() #刪除訊息
async def clean(ctx, num:int):
    await ctx.channel.purge(limit=num+1)

@bot.command()
async def daily(ctx):
    await ctx.send("@OwO#8456")
    print("I don't have daily :(")

'''======================================================================================='''

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])
