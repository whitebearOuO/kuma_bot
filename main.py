import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    
cogs_list = [
    'basic'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
    
@bot.slash_command(name="hello", description="Say hello to the bot") #hello指令
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")
    
bot.run(os.getenv('DISCORD_TOKEN')) # run the bot with the token