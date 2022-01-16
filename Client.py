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

@client.listen()
async def on_message(message):
    """
    Listens for when a message is called, and if it starts with a !, the bot will delete it
    :param message: the message sent by the user
    :type message: discord.message.Message
    :return: a DM to the user letting them know their cooldown has ended
    """
    if message.content.startswith("!"):
        await message.delete()


@client.event
async def on_ready():
    """ Sets the status of the bot when it connects to the guild """
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="The Trading Charts",
                                  url="https://www.tradingview.com/chart/ipFS446E/"))


@client.command()
async def premiumMembership(ctx):
    """
    Sends an embedded message containing all the premium membership
    :param ctx:
    :return:
    """

    # Declaration of embed header
    resource_message = discord.Embed(
        title="\tPremium Membership",
        url="https://www.tradingview.com", description="Are you ready to take your trading to the next level?"
                                                       "https://youtu.be/O9vGoh8coow",
        color=0x4EEDEB)

    # This shows the member who called the bot function
    resource_message.set_author(name=ctx.author.display_name,
                                url="https://www.tradingview.com",
                                icon_url=ctx.author.avatar_url)

    resource_message.set_thumbnail(url="https://cdn.discordapp.com/attachments/932108652561711164/932108913900400710"
                                       "/ccp.png")

    resource_message.add_field(name="CryptoCache Premium Offers"
                               , value="-Daily Bitcoin + Alt Coin Spot Signals\n-Cornix 'One Click Follow' Trading Bot "
                                       "Functionality\n-Unleveraged, Long and Short positions\n-Day Trades + Swing & "
                                       "HODL trades"
                               , inline=True)

    resource_message.add_field(name="CryptoCache Also Includes"
                               , value="\n-Entry, Profit and Stop Targets\n-Technical Analysis and Trade Set "
                                       "Ups\n-Best Practice / Market Updates and News \n-Private Telegram Group Chat"
                               , inline=True)

    resource_message.add_field(name="Premium Services Coming Soon"
                               , value="\n-Full website service for faster enrollment \n-Leverage / Futures / "
                                       "Perpetual Contracts"
                               , inline=True)

    resource_message.set_footer(text="\tYou also get direct contact with CryptoCache")

    await ctx.send(embed=resource_message)


@client.command()
async def referrals(ctx):
    """
    Sends an embedded message containing all CCs Referral
    :param ctx:
    :return:
    """

    # Declaration of embed header
    referral_message = discord.Embed(
        title="\tThe Stuff I Use",
        url="https://www.tradingview.com", description="A list of different things I use for trading, along with my "
                                                       "referral links",
        color=0x4EEDEB)

    # This shows the member who called the bot function
    referral_message.set_author(name=ctx.author.display_name,
                                url="https://www.tradingview.com",
                                icon_url=ctx.author.avatar_url)

    referral_message.set_thumbnail(url="https://cdn.discordapp.com/attachments/932108652561711164/932124740355776562/ccg2.png")

    referral_message.add_field(name="Voyager $25 BTC Referral Link:"
                               , value="https://voyager.onelink.me/WNly/referral?af_sub5=JAS3BE \nReferral Code: JAS3BE"
                               , inline=True)

    referral_message.add_field(name="Bittrex Referral Link:"
                               , value="https://bittrex.com/Account/Register?referralCode=VYH-CDK-J5I\n Referral "
                                       "Code: VYH-CDK-J5I ", inline=True)

    referral_message.add_field(name="KuCoin Referral Link:"
                               , value="https://www.kucoin.com/ucenter/signup?rcode=rJ8GB5C\nReferral Code: rJ8GB5C"
                               , inline=True)

    referral_message.add_field(name="Cornix Referal Link"
                               , value="https://t.me/cornix_trading_bot?start=ref-297c234efc6341fe91369a51421bc85d"
                               , inline=True)

    referral_message.add_field(name="Gate.Io:"
                               , value="https://www.gate.io/signup/9048506"
                               , inline=True)

    referral_message.add_field(name="TradingView $30 Referral Link:"
                               , value="https://www.tradingview.com/gopro/?share_your_love=cryptocurrent81"
                               , inline=True)

    referral_message.add_field(name="Crypto.com $25 Referral Link:"
                               , value="https://crypto.com/app/rqubt5u47p"
                               , inline=True)

    referral_message.add_field(name="Binance Referral Link:"
                               , value="https://accounts.binance.us/en/register?ref=53981797"
                               , inline=True)

    referral_message.add_field(name="Coinstats Referral Link:"
                               , value="coinstats.app/pricing?promo=cryptocache"
                               , inline=True)


    await ctx.send(embed=referral_message)


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
async def member(ctx):
    """
    Defines the ability for a user to call '!members' in a channel and the bot will return a list of all members
    organized into two columns. The end of the message displays the total number of members in each role.
    :param ctx: represents the context in which a command is being invoked under
    :return: an embedded message displaying all the users, and how many are in each role
    """

    # Captures all members in the guild, and lists them in alphabetical order
    all_members = get_all_members()

    # defines guild role IDs
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
    members_message.add_field(name="Current member count ".title(), value=str(len(all_members)), inline=True)
    members_message.add_field(name="Number of Premium Users".title(), value=str(len(premium_users.members)),
                              inline=True)
    members_message.add_field(name="Number of Non-Premium Users".title(), value=str(non_premium_users), inline=False)
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

    return list_of_members


# Allows the bot to continually run
client.run(BOT_TOKEN)
