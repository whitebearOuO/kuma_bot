import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import os
import time

bot = commands.Bot(command_prefix='owo ') #呼叫bot的方法 owo

'''======================================================================================='''
    
@bot.event #這裡的會在小黑窗出來
async def on_ready():
    print('logging as') 
    print(bot.user.name) #bot的名字 kuma
    print(bot.user.id) #bot的id 70啥的
    print('------')
    
'''======================================================================================='''

@bot.event
async def on_member_join(member):
	print(f'{member} join!')
	channel = bot.get_channel(711411107738288160)
	await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
	print(f'{member} leave!')
	channel = bot.get_channel(711411107738288160)
	await channel.send(f'{member} leave!')
    
@bot.command()
async def covid19(ctx): #武漢肺炎確診人數
    article_href = []
    r = requests.get("https://nidss.cdc.gov.tw/ch/NIDSS_DiseaseMap.aspx?dc=1&dt=5&disease=19CoV")
    s = r.text[r.text.find('<span id="ctl00_NIDSSContentPlace_Table">'):].split('\n')[0]
    soup = BeautifulSoup(s,"html.parser")
    th = [i.find("th").text for i in soup.find_all("tr")[1:]]
    td = [i.find("td").text for i in soup.find_all("tr")[1:-1]] + [soup.find_all("th")[-1].text]
    output = ["{} {}".format(i,j) for i,j in zip(th,td)]
    print('\n'.join(output))
    await ctx.send('\n'.join(output))
    
@bot.command()
async def add_diary(ctx, date, title,* , content): #增加日記
    with open("diary/"+date, 'w') as f:
        print(title, content, sep= '\n', file = f)
    await ctx.send('done')
    
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
    
@bot.command() #說hello owo
async def hello(ctx):
    await ctx.send("hello owo")
    
'''======================================================================================='''

@bot.command()
async def info(ctx): #詳細資訊 但其實不怎麼詳細
    embed=discord.Embed(title="kuma", url="https://discord.com/api/oauth2/authorize?client_id=708881902135672884&permissions=522304&scope=bot", description="一個測試中的bot owo", color=0x37e1dd)
    embed.set_author(name="白熊", url="https://whitebearouob.blogspot.com/", icon_url="https://1.bp.blogspot.com/-73sa6KNYNEw/XXSaqPkzW9I/AAAAAAAABPE/FQkgJuHgfyceHMON48eMDy8GLkMv9LeMQCLcBGAs/s1600/1518182898346.png")
    embed.set_thumbnail(url="https://images6.alphacoders.com/674/674742.jpg")
    embed.add_field(name="入侵幾個伺服器了owo", value=f"{len(bot.guilds)}")
    embed.add_field(name="可...可惡", value="bot好難寫owo", inline=False)
    await ctx.send(embed=embed)
    
bot.remove_command('help') #篩除原本的help
@bot.command()
async def help(ctx): #我自己的help OuO
    embed=discord.Embed(title="那個神奇的help選單OuO", description="所有的指令開頭都是owo喔", color=0x37e1dd)
    embed.set_thumbnail(url="https://images6.alphacoders.com/674/674742.jpg")
    embed.add_field(name="owo help", value="跳出help清單", inline=False)
    embed.add_field(name="owo info", value="有關bot的資訊", inline=False)
    embed.add_field(name="owo add_diary [title] [date] [content] ", value="紀錄日記(標題不可有空白，內容可以)", inline=False)
    embed.add_field(name="owo view title [title]", value="以標題去搜尋日記", inline=False)
    embed.add_field(name="owo view date [date]", value="以日期去搜尋日記", inline=False)
    embed.add_field(name="owo covid19", value="查看目前武漢肺炎人數", inline=False)
    embed.add_field(name="owo ping", value="眾所皆知的ping就不用解釋ㄌㄅ", inline=False)
    embed.set_footer(text="指令持續增加中owo")
    await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
	await ctx.send("ping是...")
	await ctx.send(f"`{round(bot.latency*1000) }ms` owo")
	#await message.edit(content=f"Pong!  `{round(bot.latency*1000)}ms`")
    #round 小數點四捨五入

"""    
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')
    embed=discord.Embed(color=0x37e1dd)
    embed.add_field(name=f"**ping:** {int(ping)}ms", value="", inline=False)
    await ctx.send(embed=embed)
"""

'''======================================================================================='''

bot.run('NzA4ODgxOTAyMTM1NjcyODg0.Xrd0aw.qrBvJWs4bCG5mWgmgrwRlr70-Oo')
