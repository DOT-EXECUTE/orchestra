from discord.ext import commands
from dotenv import load_dotenv
import discord
import logging
import os

# ===========================
# 		Setup the bot
# ===========================

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("discord.log", encoding='utf-8', mode='w'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True # Ensure member intent is enabled in Discord Developer Portal

bot = commands.Bot(command_prefix=">>", intents=intents) # For slash commands check our docs
# bot.remove_command("help")  UNCOMMENT FOR A CUSTOM HELP COMMAND

# ======================
#        Events
# ======================

@bot.event
async def on_ready():
    logger.info(f'{bot.user} has connected to Discord!')
    logger.info(f'Connected to {len(bot.guilds)} guilds.')
    
# ======================
#     Bot Commands
# ======================

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}")

# ======================
# 	  Main Execution
# ======================

if not TOKEN:
    print("Token not set in .env . Please set it")
else:
	bot.run(TOKEN)
