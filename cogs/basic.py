import discord
from discord.ext import commands

class Basic(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

#------------------
# ping, math
#------------------

    @discord.slash_command(name="ping", description="測試bot延遲")
    async def ping(ctx: discord.ApplicationContext):
        await ctx.respond(f"{round(bot.latency*1000)} ms", ephemeral=True)

    math = discord.SlashCommandGroup("math", "讓bot代替你當計算機") # create a Slash Command Group called "math"
    advanced_math = math.create_subgroup(
        "advanced",
        "super hard math commands!"
    )

    @math.command(name="addition", description="加法")
    async def add(self, ctx, a: float, b: float):
        a = int(a) if a.is_integer() else a
        b = int(b) if b.is_integer() else b
        c = a + b
        c = int(c) if c.is_integer() else c
        await ctx.respond(f"{a} + {b} = {c}", ephemeral=True)
        
    @math.command(name="subtraction", description="減法")
    async def sub(self, ctx, a: float, b: float):
        a = int(a) if a.is_integer() else a
        b = int(b) if b.is_integer() else b
        c = a - b
        c = int(c) if c.is_integer() else c
        await ctx.respond(f"{a} - {b} = {c}", ephemeral=True)
    
    @advanced_math.command()
    async def midpoint(self, ctx, x1: float, y1: float, x2: float, y2: float):
        mid_x = (x1 + x2)/2
        mid_y = (y1 + y2)/2
        await ctx.respond(f"The midpoint between those coordinates is ({mid_x}, {mid_y}).", ephemeral=True)

def setup(bot):
    bot.add_cog(Basic(bot)) # add the cog to the bot