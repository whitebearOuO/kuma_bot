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

'''======================================================================================='''

# event

@bot.event #這裡的會在小黑窗出來
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Minecraft 111學年度先行版學習歷程更新"))
    print('logging as') 
    print(bot.user.name) #bot的名字 kuma
    print(bot.user.id) #bot的id 70啥的
    print('------')

'''======================================================================================='''

# Cog_Extension 指令

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
        break

'''======================================================================================='''

# help指令

bot.remove_command('help') #刪除原本的help
@bot.command()
async def help(ctx): #自訂help
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
    print("已送出help列表")

'''======================================================================================='''

#ping
@bot.command()
async def ping(ctx):
    message = await ctx.send("ping是...")
    p = round(bot.latency*1000)
    await message.edit(content= f"`{p }ms` owo")
    print(f"`{p }ms` owo")
    #round 小數點四捨五入

#隨機狐狸照片
@bot.command()
async def fox(ctx):
    random_pic = random.choice(jdata['url_pic'])
    await ctx.send(random_pic)

#複誦訊息
@bot.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

#刪除訊息
@bot.command()
async def clean(ctx, num:int):
    await ctx.channel.purge(limit=num+1)

'''=======================================================================================

# 無效指令(在replit上無法運行)

@bot.command()
async def add_diary(ctx, title, date,* , content): #增加日記
    with open("diary/"+title, 'w') as f:
        print(date, content, sep= '\n', file = f)
    await ctx.send('done')
    print("日記增加完成owo")
    
@bot.command()
async def view(ctx, which, info): #查看日記
    if which == 'title':
        files = os.listdir("diary")
        for i in files:
            path = "diary/"+i
            s = open(path, 'r').read()
            title = s.split('\n')[0]
            if title == info:
                await ctx.send(s)
    elif which == 'date':
        files = os.listdir("diary")
        if info in files:
            #s = open("diary/"+info, 'r').read()
            f = open("diary/"+info, 'r')
            s = f.read()
            f.close()
            await ctx.send(s)
    print("成功查看日記owo")

@bot.command()
async def upload(ctx, tag, date): #上傳圖片
    response = requests.get(ctx.message.attachments[0].url)
    file = open("picture/"+tag+" "+date+".jpg", "wb")
    file.write(response.content)
    file.close()
    await ctx.send("圖片儲存完成owo")
    print("圖片已儲存")

@bot.command()
async def search_pic(ctx, info): #搜尋圖片
    files = os.listdir("picture")
    for i in files:
        tmp = i.split()
        if info == tmp[0] or info+".jpg" == tmp[1]:
            with open("picture/"+i, 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file = picture)

======================================================================================='''

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])