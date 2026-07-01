# imports
import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from random import choice

# initialize
load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="lemon!", intents = intents)

# commands
@bot.tree.command(name = "ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! Bot is running with {round(bot.latency * 1000)} miliseconds latency.")

@bot.tree.command(name="topic", description="Get a random topic to talk about")
@app_commands.describe(pings="Users to mention")
async def topic(interaction: discord.Interaction, pings: discord.Role = None):
    topics = [
        "*taps mic* yo is this shit working?"
    ]

    if pings is not None:
        if pings.is_default() and not interaction.user.guild_permissions.mention_everyone: # if trying to ping everyone and don't have permissions to ping everyone
            await interaction.response.send_message("You don't have permission to mention everyone.", ephemeral=True)
            return

    embed = discord.Embed(title="Topic", description=choice(topics), color=discord.Color.yellow())
    await interaction.response.send_message(embed=embed, content=pings.mention if pings else None)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

bot.run(os.getenv("TOKEN"))