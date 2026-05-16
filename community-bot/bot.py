import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load token from .env file
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix='!',          # Commands start with !
    intents=intents,
    help_command=None            # We'll make a custom help command
)

# Load all cogs (command categories)
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'✅ Loaded: {filename}')

# When bot is ready
@bot.event
async def on_ready():
    await load_cogs()
    await bot.tree.sync()        # Sync slash commands
    print(f'🚀 {bot.user} is online!')
    print(f'📡 Connected to {len(bot.guilds)} server(s)')
    
    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="builders build 🔥"
        )
    )

# Slash command example
@bot.tree.command(name="ping", description="Check if bot is alive")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(
        f"🏓 Pong! Bot latency: **{latency}ms**",
        ephemeral=True  # Only visible to the user who ran it
    )
# Run the bot
bot.run(TOKEN)
