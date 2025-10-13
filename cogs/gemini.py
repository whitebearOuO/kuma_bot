import discord
from discord.ext import commands
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Gemini(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conversations = {} # 用來儲存每個使用者的對話紀錄

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if self.bot.user.mentioned_in(message):
            user_id = message.author.id
            if user_id not in self.conversations:
                self.conversations[user_id] = genai.GenerativeModel('gemini-2.5-flash').start_chat(history=[])

            try:
                async with message.channel.typing():
                    chat = self.conversations[user_id]
                    response = await chat.send_message_async(message.content)
                    await message.reply(response.text)
            except Exception as e:
                await message.reply(f"抱歉，發生了一個錯誤：{e}")


def setup(bot):
    bot.add_cog(Gemini(bot))