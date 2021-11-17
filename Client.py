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
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="The Trading Charts",
                                  url="https://www.tradingview.com/chart/ipFS446E/"))


@client.command()
async def resources(ctx):
    """
    Sends an embedded message containing all the resources for the guild
    :param ctx:
    :return:
    """

    # Declaration of embed header
    resource_message = discord.Embed(
        title="\tResource List",
        url="https://www.tradingview.com", description="Here are a compilation of resources .... ",
        color=0x4EEDEB)

    # This shows the member who called the bot function
    resource_message.set_author(name=ctx.author.display_name,
                                url="https://www.tradingview.com",
                                icon_url=ctx.author.avatar_url)

    # Declaration of field headers
    resource_message.add_field(name="How to setup cornix".title(), value="Please follow the linked guide below",
                               inline=False)
    resource_message.add_field(name="Trader view settings".title(), value="Here are my settings used on "
                                                                          "https://www.tradingview.com", inline=False)
    resource_message.add_field(name="Blank", value="text", inline=False)

    await ctx.send(embed=resource_message)


@client.command()
async def command(ctx):
    """
    Defines the ability for a user to call '!command' in a channel and the bot will return a list of all command calls
    along with the description of each call
    :param ctx: represents the context in which a command is being invoked under
    :return: returns a message from the bot that has all the commands and their descriptions
    """
    command_message = discord.Embed(
        title="CryptoCache Command Help",
        description="Here is a list of the different bot commands that you may use to call on me!",
        color=0xF70C1C)

    # This shows the member who called the bot function
    command_message.set_author(name=ctx.author.display_name,
                               url="https://www.tradingview.com",
                               icon_url=ctx.author.avatar_url)

    # Defines the contents of each field in the embed message
    command_message.add_field(name="!members",
                              value="This command returns the total amount of members in each role", inline=False)

    command_message.add_field(name="!resources",
                              value="This command returns different resources", inline=False)

    await ctx.send(embed=command_message)


@client.command()
async def members(ctx):
    """
    Defines the ability for a user to call '!members' in a channel and the bot will return a list of all members
    organized into two columns. The end of the message displays the total number of members in each role.
    :param ctx: represents the context in which a command is being invoked under
    :return: an embedded message displaying all the users, and how many are in each role
    """

    # Captures all members in the guild, and lists them in alphabetical order
    all_members = get_all_members()

    # defines guild role IDs
    owners = ctx.guild.get_role(841106848462536724)
    admins = ctx.guild.get_role(841106849130086440)
    premium_users = ctx.guild.get_role(908195543468109836)
    non_premium_users = (len(all_members) - len(premium_users.members))

    # Declaration of embed header
    members_message = discord.Embed(
        title="\tCurrent Members List",
        url="https://www.tradingview.com",
        color=0x4EEDEB)

    # This shows the member who called the bot function
    members_message.set_author(name=ctx.author.display_name,
                               url="https://www.tradingview.com",
                               icon_url=ctx.author.avatar_url)

    # Shows the total amount of users in each role
    members_message.add_field(name="Current member count ".title(), value=str(len(all_members)), inline=False)
    members_message.add_field(name="Number of Premium Users".title(), value=str(len(premium_users.members)),
                              inline=True)
    members_message.add_field(name="Number of Non-Premium Users".title(), value=str(non_premium_users), inline=True)
    await ctx.send(embed=members_message)


def get_all_members():
    """
    Gets each member in the guild, and puts them into a list
    :return: A list of users currently in the server
    """
    list_of_members = []  # Declaration of empty list

    # prints out each user in the guild
    for each_guild in client.guilds:
        for each_member in each_guild.members:
            list_of_members.append(str(each_member))  # adds the member

    remove_all_bots(list_of_members)

    return list_of_members


def remove_all_bots(list_of_members):
    """
    Removes all the bots recorded in the server
    :param list_of_members: a list of all members visible to the bot in the guild
    :return: nothing
    """
    list_of_members.remove("AXVin#4169")
    list_of_members.remove("Cornix Trading Bot#7084")
    list_of_members.remove("MEE6#4876")
    list_of_members.remove("Pingcord#3283")
    list_of_members.remove("ServerStats#0197")
    list_of_members.remove("CryptoCache Bot#3622")
    list_of_members.remove("Integromat#3989")


# Allows the bot to continually run
client.run(BOT_TOKEN)
