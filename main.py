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
        "Water before AND after toothpaste.",
        "A hotdog is NOT a sandwich.",
        "Never have to sleep, eat, or breathe?",
        "SOCK SOCK SHOE SHOE ALWAYS",
        "i hate thin crust",
        "waffles are just grilled pancakes",
        "boneless wings = chicken nuggets",
        "pancakes > waffles",
        "will gta 6 or weaponfall season 2 come out first?"
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