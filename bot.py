import discord
from discord.ext import commands
import random

# Create bot with command prefix
bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

# Sample Microsoft account list (replace with your actual accounts)
MICROSOFT_ACCOUNTS = [
    "account1@microsoft.com",
    "account2@microsoft.com",
    "account3@microsoft.com",
    "account4@microsoft.com",
    "account5@microsoft.com",
]

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="drops", description="Drops a random Microsoft account")
async def drops(interaction: discord.Interaction):
    """Slash command that drops a random Microsoft account"""
    if not MICROSOFT_ACCOUNTS:
        await interaction.response.send_message("No accounts available!", ephemeral=True)
        return
    
    dropped_account = random.choice(MICROSOFT_ACCOUNTS)
    
    embed = discord.Embed(
        title="🎁 Account Dropped!",
        description=f"```{dropped_account}```",
        color=discord.Color.blue()
    )
    embed.set_footer(text=f"Dropped by {interaction.user.name}")
    
    await interaction.response.send_message(embed=embed)

# Replace 'YOUR_TOKEN_HERE' with your actual bot token
bot.run('YOUR_TOKEN_HERE')
