# bot.py
import os

import discord
from discord.ext import commands, tasks
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

if TOKEN is None:
    raise ValueError("Bot token not found")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def remind(ctx, day, hours: int, minutes: int, *, text):
    
    day_seconds = 0 if day == "." else int(day)*86400 
    
    delay_seconds =day_seconds + hours * 3600 + minutes * 60

    await ctx.send(f"Okay {ctx.author.mention}, I'll remind you in {hours}h {minutes}m!")

    await asyncio.sleep(delay_seconds)

    await ctx.channel.send(f"⏲ Hey {ctx.author.mention}, reminder: {text}")

bot.run(TOKEN)
    