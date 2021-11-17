"""  """
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

# Loads the encapsulated values from the .env file
load_dotenv()

# Declaration of Encapsulated Variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Declaration Discord.py Variables
intents = discord.Intents.default()  # Turns on the connection
intents.members = True  # Ensures the member list will be updated properly
client = commands.Bot(command_prefix='!', intents=intents)  # defines the symbol used to call a command from the bot


@client.event
async def on_ready():
    """ Sets the status of the bot when it connects to the guild """
    await client.change_presence(activity=discord.Game('RDO - Wagon Stealing'))  # sets the bots activity status