import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import (CommandOnCooldown)
from PIL import Image, ImageFont, ImageDraw, ImageOps
from unidecode import unidecode
from io import BytesIO
import asyncio
import discord.utils
import functools
from discord.utils import get
import discord, datetime, time
from discord.ext import commands
import math
import wiki
import os
import keep_alive
import wikipedia
import traceback
import random
import json
import utils
from discord.utils import find
import datetime
from datetime import datetime, timedelta
from platform import python_version
from replit import db
from time import time
import discord
from discord.ext import commands, tasks
from io import BytesIO
import datetime
from datetime import datetime

from discord.ext import commands
intents = discord.Intents.default()

from PIL import Image
from io import BytesIO

intents.members = True

client = commands.Bot(
    command_prefix='!', case_insensitive=True, intents=intents)
from io import BytesIO


def time_encode(sec):
    time_type, newsec = 'seconds', int(sec)
    if sec > 60:
        newsec, time_type = round(sec / 60), 'minutes'
        if sec > 3600:
            newsec, time_type = round(sec / 3600), 'hours'
            if sec > 86400:
                newsec, time_type = round(sec / 86400), 'days'
                if sec > 2592000:
                    newsec, time_type = round(sec / 2592000), 'months'
                    if sec > 31536000:
                        newsec, time_type = round(sec / 31536000), 'years'
    if str(newsec) == '1': return str(str(newsec) + ' ' + time_type[:-1])
    return str(str(newsec) + ' ' + time_type)


for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')


@client.command(hidden=True)
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully loaded module')


@client.command(hidden=True)
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully unloaded module')


@client.command(hidden=True)
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f'Cogs.{extension}')
    await ctx.send('Succesfully reloaded module')


class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(CogName(bot))


@client.event
async def on_message(msg):

    try:
        if msg.mentions[0] == client.user:

            await msg.channel.send(f"My prefix is !")

    except:
        pass

    await client.process_commands(msg)


@client.event
async def on_guild_join(guild):
    channel = client.get_channel(789032560500015114)
    embed = discord.Embed(
        title="I Joined a new server",
        description=
        f"Name: {guild},\nMembers: {guild.member_count}\nid: {guild.id} \nOwner: {guild.owner}"
    )
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f"{len(client.guilds)} servers.")
    await channel.send(embed=embed)


@client.event
async def on_guild_remove(guild):
    channel = client.get_channel(789032560500015114)
    embed = discord.Embed(
        title="I was removed from a server",
        description=
        f"Name: {guild},\nMembers: {guild.member_count}id: {guild.id}")
    embed.set_thumbnail(url=guild.icon_url)
    embed.set_footer(text=f"{len(client.guilds)} servers.")

    await channel.send(embed=embed)


filtered_words = ["asshole", "wtf", "fuck", "fuck you", "fck", "fuck off"]


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')

    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)


def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)


@client.event
async def on_ready():
    global startdate
    startdate = datetime.now()


@client.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title=f"***{error}***")
    await ctx.send(embed=embed)
    print(error)
    raise error


class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(
                    f"{argument} is not a valid member or member ID."
                ) from None
        else:
            return m.id


@client.command()
#@client.has_permissions(administrator = True)
async def embed(ctx, *, channel: discord.TextChannel):
    await ctx.send("Send me a title for the embed")

    def check(message):
        return (message.author == ctx.author and message.channel == ctx.channel
                and not message.author.bot)

    try:
        msg = await client.wait_for("message", timeout=60.0, check=check)

    except asyncio.TimeoutError:
        return await ctx.send("No title was provided time up")

    else:
        t = msg.content
        if t.content.lower() == "none":
            tit = None
        else:
            tit = t

        await ctx.send("Now send me the text you want to be in the embed")

    try:
        msg = await client.wait_for("message", timeout=60.0, check=check)
    except asyncio.TimeoutError:
        return await ctx.send("No description was provided")
    else:
        desc = msg.content
        await ctx.send("all set")

    embed = discord.Embed(title=tit, description=desc, colour=0x00c8ff)
    if len(msg.attachments) > 0:
        embed.set_image(url=msg.attachments[0].url)

    await channel.send(embed=embed)


@client.command()
async def hey(ctx):
    await ctx.send("Hello")


@client.command()
async def good_day(ctx):
    await ctx.send("Have a really good and a productive day")


@client.command()
async def hi(ctx):
    await ctx.send("Hey")


@client.command()
async def hello(ctx):
    await ctx.send("Hi wassup")


@client.command()
async def invite(ctx):
    embed = discord.Embed(
        title="Information about the bot", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/566193564502196235/b624ea7737776938c070f6693c91abc9?size=2048"
    )
    embed.add_field(
        name="Invite",
        value=
        "[Invite the bot](https://discord.com/oauth2/authorize?client_id=760415780176658442&permissions=8&scope=bot)",
        inline=False)
    embed.add_field(
        name="Community Server",
        value="[Join the Community Server](https://discord.gg/4fNdfNjKd9)",
        inline=False)

    await ctx.send(embed=embed)


@client.command(aliases=["stats"])
async def info(ctx):
    embed = discord.Embed(
        title="Information about the bot", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/771998022807584797/785758835066667008/White_Red_and_Orange_Badge_Recess_Food_Festival_Logo_3.gif'
    )
    embed.add_field(name="Name", value="RKS", inline=False)
    embed.add_field(name="Developing Language", value="Python", inline=False)
    embed.add_field(
        name="Developed By", value="<@566193564502196235>", inline=False)
    embed.add_field(
        name="Help",
        value="use !help command to get to know about the other commands",
        inline=False)
    embed.add_field(
        name="Invite",
        value=
        "[Invite the bot](https://discord.com/oauth2/authorize?client_id=760415780176658442&permissions=8&scope=bot)",
        inline=False)
    embed.add_field(
        name="Community Server",
        value="[Join the Community Server](https://discord.gg/4fNdfNjKd9)",
        inline=False)
    embed.add_field(
        name="Website",
        value=
        "[Bot's Official Website](https://rksbot.netlify.app/) \n [Vote for RKS](https://top.gg/bot/760415780176658442/vote)",
        inline=False)
    embed.add_field(
        name="Servers RKS getting used on",
        value=f"{len(client.guilds)} servers.",
        inline=False)
    embed.add_field(
        name="RKS Users", value=f"{len(client.users)} Users.", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def Bots(ctx):
    embed = discord.Embed(
        title="Bots \n \n Spotify Bot - $75 BTC \n Twitch Bot - $85 BTC",
        colour=discord.Colour.blue())
    await ctx.send(embed=embed)


@client.command()
async def dev_info(ctx):
    embed = discord.Embed(
        title="Developing information about the bot",
        colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        'https://cdn.discordapp.com/attachments/771998022807584797/785758835066667008/White_Red_and_Orange_Badge_Recess_Food_Festival_Logo_3.gif'
    )
    embed.add_field(name="Name", value="RKS", inline=False)
    embed.add_field(name="Developing Language", value="Python", inline=False)
    embed.add_field(
        name="Developed By", value="Aryaman Srivastava", inline=False)
    embed.add_field(
        name="Help",
        value="use !help command to get to know about the other commands",
        inline=False)
    embed.add_field(
        name="Invite",
        value=
        "[Invite the bot](https://discord.com/oauth2/authorize?client_id=760415780176658442&permissions=8&scope=bot)",
        inline=False)
    embed.add_field(
        name="Community Server",
        value="[Join the Community Server](https://discord.gg/4fNdfNjKd9)",
        inline=False)
    embed.add_field(
        name="Servers RKS getting used on",
        value=f"{len(client.guilds)} servers.",
        inline=False)
    embed.add_field(name="Bot Created On", value="Repl.it", inline=False)
    embed.add_field(
        name="Running 24/7 ", value="Google Cloud Console", inline=False)
    embed.add_field(name="Python Version", value="3.8.2", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def gm(ctx):
    await ctx.send("good morning,have a great day")


@client.command()
async def wassup(ctx):
    await ctx.send("I am Bored, what about you?")


@client.command(aliases=["Good Morning"])
async def good_morning(ctx):
    await ctx.send("Good Morning")


@client.command()
async def bored(ctx):
    await ctx.send(
        "Here are somethings you can do https://www.arkadium.com/free-online-games/ or listen to some songs? https://www.spotify.com/in/ or maybe some videos https://www.youtube.com/"
    )


@client.command()
async def rule1(ctx):
    await ctx.send(
        "Welcome, Witness me peform some tasks,I am RKS, nice to meet you.")


@client.command()
async def gn(ctx):
    await ctx.send("Good night, Have sweet dreams ")


@client.command()
async def games(ctx):
    await ctx.send("https://www.arkadium.com/free-online-games/")


@client.command()
async def songs(ctx):
    await ctx.send("https://www.spotify.com/in/")


@client.command()
async def Sports(ctx):
    embed = discord.Embed(
        title="Sports news and live scored", colour=discord.Colour.blue())
    embed.add_field(
        name="Football",
        value=
        "Find all football news and scores on https://www.espn.in/football/scoreboard",
        inline=False)
    embed.add_field(
        name="Cricket",
        value="Find all cricket news and scores on https://www.cricbuzz.com/")
    embed.add_field(
        name="BasketBall",
        value=
        "Find all BasketbaLL news and scores on https://in.nba.com/?gr=www")
    await ctx.send(embed=embed)


@client.command()
async def talk(ctx):
    await ctx.send(
        "Hi i am RKS, i would love to talk to you..so what do you want to talk about"
    )


@client.command()
async def life(ctx):
    await ctx.send("Ok..how is life going? You happy or sad?")


@client.command()
async def news(ctx):
    await ctx.send(
        "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")


@client.command()
async def happy(ctx):
    await ctx.send("Wow, nice to know..i am happy that you are enjoying life")


@client.command()
async def weather(ctx):
    await ctx.send("https://www.accuweather.com/")


@client.command()
async def videos(ctx):
    await ctx.send("https://www.youtube.com/")


@client.command()
async def game(ctx):
    await ctx.send(
        "Among us (Mobile & PC/Laptop) \nValorant(PC/laptop) \nCall of duty (Mobile/laptop)\nGrand Theft Auto (Laptop),\nGetting over it (Laptop)"
    )


@tasks.loop(seconds=500)
async def status_change():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name="@AryamanSri#0001"))
    await asyncio.sleep(500)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="https://rksbot.netlify.app/"))
    await asyncio.sleep(500)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.Updating, name="RKS Version 1.07"))
    await asyncio.sleep(500)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=f"{len(client.users)} users."))
    await asyncio.sleep(500)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(client.guilds)} servers."))
    await asyncio.sleep(500)


status_change.before_loop(client.wait_until_ready)
status_change.start()

client.remove_command("help")


@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="RKS COMMANDS 🤖", colour=discord.Colour.blue())

    embed.add_field(
        name="Moderation 💂‍♀️",
        value=
        "`announcerole, ban, kick, find, massban, mute, unmute, prune, lock, unlock, cooldown, warn, checkwarns, removewarn`  ",
        inline=True)
    embed.add_field(
        name="Talking 🤷🏻‍♂️", value="`!Hi !Hey !Hello wassup bored` ")
    embed.add_field(name="Sports 🏆", value="`!sports`")
    embed.add_field(name="Greetings ✌️", value="`!gm !gn !good_day`")
    embed.add_field(
        name="Information Commands 🔎",
        value=
        "`!info !dev_info !server_info !whois/!userinfo !suggest report !unlock` "
    )
    embed.add_field(
        name="Clock ⏰",
        value="`!timer{time in seconds} !remind{time in mins,reminder name}`")
    embed.add_field(
        name="Important Links :link:",
        value=
        "[Invite the bot](https://discord.com/oauth2/authorize?client_id=760415780176658442&permissions=8&scope=bot) \n [Join the Community Server](https://discord.gg/4fNdfNjKd9) \n [Bot's Official Website](https://rksbot.netlify.app/) \n [Vote for RKS](https://top.gg/bot/760415780176658442/vote)"
    )
    embed.add_field(
        name="Total Commands",
        value=f"{len([x.name for x in client.commands])}",
        inline=True)
    embed.add_field(
        name="Fun Commands 🥳",
        value=
        "`!treat` `!ping` `!gayrate` `!quote` `ball` `!shrug` `Tableflip` `UNFLIP`"
    )
    embed.add_field(
        name="Music 🎶",
        value=
        "`!play{songname}` `!stop` `!pause` `!resume` `!np` `!skip` `!queue` `!shuffle`"
    )
    embed.add_field(name="Chatbot 🧍🏻‍♂️🧍🏻", value="`!rks{anything}` ")
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif'
    )
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def ping(ctx):
    """ Pong! """
    before = time.monotonic()
    message = await ctx.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!🏓 \n `{int(ping)}ms`")
    print(f'Ping {int(ping)}ms')


@client.command()
async def Moderation(ctx):
    embed = discord.Embed(
        title="All Moderation Commands", colour=discord.Colour.blue())
    embed.add_field(name="!mute", value="Mutes the user{@user}", inline=False)
    embed.add_field(
        name="!unmute{@user}", value="Unmutes the user", inline=False)
    embed.add_field(
        name="!kick{@user}",
        value="Kicks the user from the server",
        inline=False)
    embed.add_field(
        name="!ban{@user}",
        value="Bans the user from the server",
        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def help_greetings(ctx):
    embed = discord.Embed(
        title="All Greeting Commands", colour=discord.Colour.blue())
    embed.add_field(
        name="Greeting",
        value=
        "!gm: Wishes the user Good Morning \n !gn:Wishes the user Good Night  \n !good_day: Wishes the user a good day",
        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def Talking(ctx):
    embed = discord.Embed(
        title="All Talking Commands", colour=discord.Colour.blue())
    embed.add_field(
        name="Talking",
        value=
        "!Hello: Wishes the user Hello \n !Hey:Wishes the user Hey  \n !wassup: Bot will reply with what it is doing \n !info: Inddormation about the bot \n !Bored: Bot will send somethings you can do to pass time \n !Music: Bot plays some awesome english songs \n !Hi:Wishes the user Hi",
        inline=False)
    await ctx.send(embed=embed)


@client.command()
async def Server(ctx):
    embed = discord.Embed(title="Servers", colour=discord.Colour.blue())
    embed.add_field(
        name="Servers RKS getting used on",
        value=f"{len(client.guilds)} servers.",
        inline=False)
    embed.add_field(
        name="User's Using RKS",
        value=f"{len(client.users)} users.",
        inline=False)

    await ctx.send(embed=embed)


@client.command()
async def Mentor(ctx):
    embed = discord.Embed(
        title="The Reason why bot is alive", colour=discord.Colour.blue())

    embed.add_field(name="Name", value="Krish Kharangra", inline=False)
    embed.add_field(name="UserName", value="@Kalu#7777", inline=False)
    embed.add_field(name="User ID", value="457569956079337472", inline=False)

    await ctx.send(embed=embed)


@commands.command(name='rps', aliases=['rockpaperscissors'])
async def rps(self, ctx):
    """Play Rock, Paper, Scissors game"""

    def check_win(p, b):
        if p == '🌑':
            return False if b == '📄' else True
        elif p == '📄':
            return False if b == '✂' else True
        else:  # p=='✂'
            return False if b == '🌑' else True

    async with ctx.typing():
        reactions = ['🌑', '📄', '✂']
        game_message = await ctx.send(
            "**Rock Paper Scissors**\nChoose your shape:", delete_after=15.0)
        for reaction in reactions:
            await game_message.add_reaction(reaction)
        bot_emoji = random.choice(reactions)

    def check(reaction, user):
        return user != self.bot.user and user == ctx.author and (str(
            reaction.emoji) == '🌑' or '📄' or '✂')

    try:
        reaction, user = await self.bot.wait_for(
            'reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f"Time's Up! :stopwatch:")
    else:
        await ctx.send(
            f"**:man_in_tuxedo_tone1:\t{reaction.emoji}\n:robot:\t{bot_emoji}**"
        )
        # if conds
        if str(reaction.emoji) == bot_emoji:
            await ctx.send("**It's a Tie :ribbon:**")
        elif check_win(str(reaction.emoji), bot_emoji):

            await ctx.send(
                "**You win :sparkles:\nAs a reward i will be giving you 100 coins**"
            )

        else:
            await ctx.send("**I win :robot:**")


@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    wanted = Image.Open(
        "https://cdn.discordapp.com/attachments/771998022807584797/786807994133774346/wanted-vintage-western-poster_176411-3.jpg"
    )

    asset = user.avatar_url_as(size=130)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((177, 177))

    wanted.paste(pfp, (120, 212))
    wanted.save("profile.jpg")

    await ctx.send(file=discord.File("profile.jpg"))


@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def suggest(ctx, *, sugg):
    channel = client.get_channel(788427578608189440)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title='New Suggestion By {}'.format(ctx.author.display_name))
    embed.add_field(name='Suggestion: ', value=sugg)
    embed.set_footer(
        text='UserID: ( {} ) | sID: ( {} )'.format(ctx.author.id,
                                                   ctx.author.display_name),
        icon_url=ctx.author.avatar_url)
    await ctx.send('👌| Your Suggestion Has Been Sent To <#{}> !'.format(
        channel.id))
    suggg = await channel.send(embed=embed)
    await suggg.add_reaction('👍')
    await suggg.add_reaction('👎')


@client.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def report(ctx, *, report):
    channel = client.get_channel(795182039723933706)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(
        title='New Report By {}'.format(ctx.author.display_name))
    embed.add_field(name='Issue: ', value=report)
    embed.set_footer(
        text='UserID: ( {} ) | sID: ( {} )'.format(ctx.author.id,
                                                   ctx.author.display_name),
        icon_url=ctx.author.avatar_url)
    await ctx.send(
        '👌 | Your report Has Been Sent To <#{}> !, sorry for the inconvenience'
        .format(channel.id))
    report = await channel.send(embed=embed)
    await report.add_reaction('👍')
    await report.add_reaction('👎')


@client.command(aliases=['8ball'])
async def ball(ctx, *, question):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.",
        "Better not tell you now.", "Cannot predict now.",
        "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
        "My sources say no.", "Very doubtful."
    ]
    embed = discord.Embed(
        title="8-ball",
        description=f"{random.choice(responses)}",
        color=discord.Colour.blue())
    await ctx.send(embed=embed)


@client.command(aliases=[
    'quote',
])
async def Quotes(ctx):
    responses = [
        "“The Best Way To Get Started Is To Quit Talking And Begin Doing.”",
        "“The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.”",
        "“Don’t Let Yesterday Take Up Too Much Of Today.”",
        "“You Learn More From Failure Than From Success. Don’t Let It Stop You. Failure Builds Character.”",
        "“It’s Not Whether You Get Knocked Down, It’s Whether You Get Up.”",
        " “If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.”",
        "“People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.”",
        "“Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.”",
        "“Entrepreneurs Are Great At Dealing With Uncertainty And Also Very Good At Minimizing Risk. That’s The Classic Entrepreneur.”",
        "“We May Encounter Many Defeats But We Must Not Be Defeated.”",
        "“Knowing Is Not Enough; We Must Apply. Wishing Is Not Enough; We Must Do.”",
        "“Imagine Your Life Is Perfect In Every Respect; What Would It Look Like?”",
        "“We Generate Fears While We Sit. We Overcome Them By Action.”",
        "“Whether You Think You Can Or Think You Can’t, You’re Right.”",
        "“Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.”",
        " “The Man Who Has Confidence In Himself Gains The Confidence Of Others.”",
        "“The Only Limit To Our Realization Of Tomorrow Will Be Our Doubts Of Today.”",
        "“Creativity Is Intelligence Having Fun.”",
        "“What You Lack In Talent Can Be Made Up With Desire, Hustle And Giving 110% All The Time.”"
    ]
    embed = discord.Embed(
        title="Daily Quotes",
        description=f"{random.choice(responses)}",
        color=discord.Colour.blue())
    embed.set_footer(text=f"Have a Great Day {ctx.author}")
    await ctx.send(embed=embed)


@client.command()
async def Tableflip(ctx):
    embed = discord.Embed(
        title="Requested by You", colour=discord.Colour.blue())
    embed.add_field(name="TABLEFLIP", value="(╯°□°）╯︵ ┻━┻", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)


@client.command()
async def shrug(ctx):
    embed = discord.Embed(
        title="As Requested by You", colour=discord.Colour.blue())
    embed.add_field(name="SHRUG", value="¯\_(ツ)_/¯", inline=False)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ctx.send(embed=embed)


@client.command()
async def unflip(ctx):
    embed = discord.Embed(
        title="Requested by You", colour=discord.Colour.blue())
    embed.add_field(name="UNFLIP", value="┬─┬ ノ( ゜-゜ノ)", inline=False)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ctx.send(embed=embed)


@client.command(case_insensitive=True)
async def treat(ctx, member: discord.Member):
    if member == ctx.author:
        await ctx.send("You can't treat youself!")
        return
    embed = discord.Embed(
        description=
        f'You offered {member.name} a treat!! {member.mention} react to the emoji below to accept!',
        color=0x006400)
    timeout = int(15.0)
    message = await ctx.channel.send(embed=embed)

    await message.add_reaction('🍫')
    await message.add_reaction('🍕')
    await message.add_reaction('🍰')
    await message.add_reaction('🍦')
    await message.add_reaction('🍔')

    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍫'

    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍕'

    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍰'

    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍦'

    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍔'

    try:
        reaction, user = await client.wait_for(
            'reaction_add', timeout=timeout, check=check)

    except asyncio.TimeoutError:
        msg = (f"{member.mention} didn't accept the treat in time!!")
        await ctx.channel.send(msg)

    else:
        await ctx.channel.send(
            f"{member.mention} You have accepted {ctx.author.name}'s offer!")


@client.command()
@commands.has_permissions(kick_members=True)
async def quite(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Who do you want me to mute?")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send("ok I did it")


@client.command(aliases=['howgayy'])
async def gayrate(ctx):
    responses = [
        'You are 1 percent gay.', 'You are 2 percent gay.',
        'You are 3 percent gay.', 'You are 4 percent gay.',
        'You are 5 percent gay.', 'You are 6 percent gay.',
        'You are 7 percent gay.', 'You are 8 percent gay.',
        'You are 9 percent gay.', 'You are 10 percent gay.',
        'You are 11 percent gay.', 'You are 12 percent gay.',
        'You are 13 percent gay.', 'You are 14 percent gay.',
        'You are 15 percent gay.', 'You are 16 percent gay.',
        'You are 17 percent gay.', 'You are 18 percent gay.',
        'You are 19 percent gay.', 'You are 20 percent gay.',
        'You are 21 percent gay.', 'You are 22 percent gay.',
        'You are 23 percent gay.', 'You are 24 percent gay.',
        'You are 25 percent gay.', 'You are 26 percent gay.',
        'You are 27 percent gay.', 'You are 28 percent gay.',
        'You are 29 percent gay.', 'You are 30 percent gay.',
        'You are 31 percent gay.', 'You are 32 percent gay.',
        'You are 33 percent gay.', 'You are 34 percent gay.',
        'You are 35 percent gay.', 'You are 36 percent gay.',
        'You are 37 percent gay.', 'You are 38 percent gay.',
        'You are 39 percent gay.', 'You are 40 percent gay.',
        'You are 41 percent gay.', 'You are 42 percent gay.',
        'You are 43 percent gay.', 'You are 44 percent gay.',
        'You are 45 percent gay.', 'You are 46 percent gay.',
        'You are 47 percent gay.', 'You are 48 percent gay.',
        'You are 49 percent gay.', 'You are 50 percent gay.',
        'You are 51 percent gay.', 'You are 52 percent gay.',
        'You are 53 percent gay.', 'You are 54 percent gay.',
        'You are 55 percent gay.', 'You are 56 percent gay.',
        'You are 57 percent gay.', 'You are 58 percent gay.',
        'You are 59 percent gay.', 'You are 60 percent gay.',
        'You are 61 percent gay.', 'You are 62 percent gay.',
        'You are 63 percent gay.', 'You are 64 percent gay.',
        'You are 65 percent gay.', 'You are 66 percent gay.',
        'You are 67 percent gay.', 'You are 68 percent gay.',
        'You are 69 percent gay.', 'You are 70 percent gay.',
        'You are 71 percent gay.', 'You are 72 percent gay.',
        'You are 73 percent gay.', 'You are 74 percent gay.',
        'You are 75 percent gay.', 'You are 76 percent gay.',
        'You are 77 percent gay.', 'You are 78 percent gay.',
        'You are 79 percent gay.', 'You are 80 percent gay.',
        'You are 81 percent gay.', 'You are 82 percent gay.',
        'You are 83 percent gay.', 'You are 84 percent gay.',
        'You are 85 percent gay.', 'You are 86 percent gay.',
        'You are 87 percent gay.', 'You are 88 percent gay.',
        'You are 89 percent gay.', 'You are 90 percent gay.',
        'You are 91 percent gay.', 'You are 92 percent gay.',
        'You are 93 percent gay.', 'You are 94 percent gay.',
        'You are 95 percent gay.', 'You are 96 percent gay.',
        'You are 97 percent gay.', 'You are 98 percent gay.',
        'You are 99 percent gay.', 'You are 100 percent gay.'
    ]
    mbed = discord.Embed(
        title='Gay Rate', description=f'{random.choice(responses)}')
    await ctx.send(embed=mbed)


@client.command(aliases=['n'])
async def nuke(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(
        title='Success',
        description=f'{channel} has been nuked.',
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
        await channel.delete()


@client.command(aliases=['hackk'])
async def hack(ctx):
    await ctx.send('rick rolled')
    await ctx.send(
        'https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825'
    )


@client.command(aliases=['roll'])
async def diceroll(ctx):
    responses = [
        'You rolled a 1!',
        'You rolled a 2!',
        'You rolled a 3!',
        'You rolled a 4!',
        'You rolled a 5!',
        'You rolled a 6!',
    ]
    mbed = discord.Embed(
        title='Dice Rolled!', description=f'{random.choice(responses)}')
    mbed.set_thumbnail(
        url=
        'https://images-ext-2.discordapp.net/external/kAegJWUTO1muMX0U5mEKgKSmpHuNl4it6086g2F3pCw/https/gilkalai.files.wordpress.com/2017/09/dice.png?width=80&height=77'
    )
    await ctx.send(embed=mbed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def announce(ctx, ch: discord.TextChannel = None):
    if ch == None:
        await ctx.send('Channel not specified')
        return

    def check(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel

    await ctx.send('Enter the title:')
    t = await client.wait_for('message', check=check, timeout=60)
    await ctx.send('Enter the message:')
    msg = await client.wait_for('message', check=check, timeout=120)
    embed = discord.Embed(
        title=t.content, description=msg.content, color=0xffff)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ch.send(embed=embed)


@client.command()
async def update(
        ctx,
        member: discord.Member,
):

    if not member:  # if member is no mentioned
        await ctx.send("User isnt Mentioned  :grey_question:")

    def check(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel

    await ctx.send('Enter the title:')
    t = await client.wait_for('message', check=check, timeout=60)
    await ctx.send('Enter the message:')
    msg = await client.wait_for('message', check=check, timeout=120)
    embed = discord.Embed(
        title=t.content, description=msg.content, color=0xffff)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await member.send(embed=embed)


@client.command(aliases=['membercount'])
async def members(ctx):
    mbed = discord.Embed(
        color=discord.Color(0xffff), title=f'{ctx.guild.name}')
    mbed.set_thumbnail(url=f'{ctx.guild.icon_url}')
    mbed.add_field(name='Member Count', value=f'{ctx.guild.member_count}')
    mbed.set_footer(
        icon_url=f'{ctx.guild.icon_url}', text=f'Guild ID: {ctx.guild.id}')
    await ctx.send(embed=mbed)


client.remove_command("commands")


@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title="Commands Loaded", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/760415780176658442/976c9cc26755a5674b032f8acb0fef8c.png?size=128"
    )
    embed.add_field(
        name="Total Commands",
        value=f"{len([x.name for x in client.commands])}",
        inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['ticket'])
async def createchannel(ctx, channelName):
    guild = ctx.guild

    mbed = discord.Embed(
        title='Success',
        description="{} has been successfully created.".format(channelName))
    if ctx.author.guild_permissions.send_messages:
        await guild.create_text_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)


@client.command()
async def rules(ctx):
    embed = discord.Embed(
        title="Discord Terms of Service", colour=discord.Colour.blue())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/566193564502196235/b624ea7737776938c070f6693c91abc9?size=2048"
    )
    embed.add_field(
        name="Rule of Conduct",
        value=
        "Do not organize, participate in, or encourage harassment of others. Disagreements happen and are normal, but continuous, repetitive, or severe negative comments may cross the line into harassment and are not okay. \n Do not organize, promote, or coordinate servers around hate speech. It’s unacceptable to attack a person or a community based on attributes such as their race, ethnicity, national origin, sex, gender, sexual orientation, religious affiliation, or disabilities. \n Do not make threats of violence or threaten to harm others. This includes indirect threats, as well as sharing or threatening to share someone’s private personal information (also known as doxxing) \n Do not evade user blocks or server bans. Do not send unwanted, repeated friend requests or messages, especially after they’ve made it clear they don’t want to talk to you anymore.",
        inline=False)
    embed.add_field(
        name="NSFW",
        value=
        "You must apply the NSFW label to channels if there is adult content in that channel. Any content that cannot be placed in an age-gated channel, such as avatars, server banners, and invite splashes, may not contain adult content. \n You may not sexualize minors in any way. This includes sharing content or links which depict minors in a pornographic, sexually suggestive, or violent manner, and includes illustrated or digitally altered pornography that depicts minors   \n You may not share sexually explicit content of other people without their consent, or share or promote sharing of non-consensual intimate imagery in an attempt to shame or degrade someone. \n You may not share content that glorifies or promotes suicide or self-harm, including any encouragement to others to cut themselves, or embrace eating disorders such as anorexia or bulimia. \n You may not use Discord for the organization, promotion, or support of violent extremism.",
        inline=False)
    embed.add_field(
        name="Verification",
        value=
        "These rules are verified as per discord guidelines and are expected to be followed seriously",
        inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=[
    'Funfacts',
])
async def facts(ctx):
    responses = [
        "“The idea of RKS was discussed in random discord chatting”",
        "“RKS was born on 19 November ”",
        "“RKS is supposed to MEE6”",
        "“RKS is not developed by a single person. Each developer had a little contribution to make the bot success”",
    ]
    embed = discord.Embed(
        title="Fun Fact about RKS",
        description=f"{random.choice(responses)}",
        color=discord.Colour.blue())
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')(
            text=f"Have a Great Day {ctx.author}")
    await ctx.send(embed=embed)


@client.command()
async def Pet(ctx):
    embed = discord.Embed(
        title="Ok! Adopt a animals from below", colour=discord.Colour.blue())
    embed.add_field(
        name="Animals List",
        value=
        "Cat 🐈 \n Dog 🐕‍🦺 \n Goldfish 🐟 \n Hamster 🐹 \n Kitten 🐈\n Mouse 🐁 \n Parrot 🦜 \n Puppy 🐕‍🦺\n Rabbit 🐇 \n Tropical fish 🐟 \n Turtle 🐢",
        inline=False)

    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')(
            text="Use !{animalname} to adopt")

    await ctx.send(embed=embed)


@client.command()
async def dog(ctx):
    embed = discord.Embed(
        title="Ok! You want a dog!", colour=discord.Colour.blue())
    embed.add_field(
        name="Animals List",
        value=
        "Cat 🐈 \n Dog 🐕‍🦺 \n Goldfish 🐟 \n Hamster 🐹 \n Kitten 🐈\n Mouse 🐁 \n Parrot 🦜 \n Puppy 🐕‍🦺\n Rabbit 🐇 \n Tropical fish 🐟 \n Turtle 🐢",
        inline=False)

    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')(
            text="Use !{animalname} to adopt")

    await ctx.send(embed=embed)


@client.command()
async def remind(ctx, mins: int, reminder):

    embed = discord.Embed(
        title=f'Reminder set for {mins} Minute named {reminder}', )
    embed.timestamp = ctx.message.created_at
    await ctx.send(embed=embed)

    counter = 0
    while counter <= int(mins):
        counter += 1
        await asyncio.sleep(60)

        if counter == int(mins):
            embed = discord.Embed(
                title='Reminder!!',
                description=
                f"⏰{ctx.author.mention}, I have set a reminder for {mins} minutes with the reminder being for {reminder} has completed",
                colour=discord.Colour.blurple())
    embed.timestamp = ctx.message.created_at
    await ctx.send(embed=embed)


@client.command()
async def rps1v1(ctx, user: discord.Member):
    try:

        def check(message) -> bool:
            return user == message.author

        await ctx.send(
            f"Okay! It\'s gonna be a game between {ctx.author.mention} and {user.mention}"
        )
        await ctx.send(
            f"{user.mention}, Reply with a ``yes`` or ``no`` to confirm your participation"
        )
        message = await client.wait_for("message", timeout=20, check=check)
    except asyncio.TimeoutError:
        await ctx.send(f"{user.mention} doesn't wanna have a game")
    else:
        if message.content == "no":
            await ctx.send("Alright let's just pretend that never happened")
        if message.content == "yes":
            await ctx.send("alright")
            player1 = ctx.author
            player2 = user
            await ctx.send(
                "alright , DM me your choices, **ONLY WHEN I ASK FOR IT**, within 30 seconds"
            )
            await player1.send(
                "Choose now, ``stone`` or ``paper`` or ``scissors``?")
            try:

                def player1_check(message) -> bool:
                    return player1 == message.author

                player1_choice = await client.wait_for(
                    "message", timeout=30, check=player1_check)
                await player1.send(
                    f"ok u chose {player1_choice.content}, I am now waiting for {player2} to choose"
                )
            except asyncio.TimeoutError:
                await player1.send("OK u dont wanna play U LOSE")
                await ctx.send(
                    f"{player1.mention} DIDNT REPLY SO HE IS A LOSER!, CONGRATS {player2.mention}, YOU WON!"
                )
            else:
                try:

                    def player2_check(message) -> bool:
                        return player2 == message.author

                    await player2.send(
                        f"Choose now, ``stone`` or ``paper`` or ``scissors``?")
                    player2_choice = await client.wait_for(
                        "message", timeout=30, check=player2_check)
                    await player2.send(f"ok u chose {player2_choice.content} ")
                except asyncio.TimeoutError:
                    await ctx.send(
                        f"{player2.mention} DIDNT REPLY SO HE IS A LOSER!, CONGRATS {player1.mention}, YOU WON!"
                    )
                    await player2.send("LOSER")
                else:
                    if player1_choice.content == player2_choice.content:
                        await ctx.send(
                            f"ITS A TIE!!! {player1.mention} chose {player1_choice.content} and {player2.mention} chose {player2_choice.content}!!!"
                        )
                    if player1_choice == "stone":
                        if player2_choice.content == "scissors":
                            await ctx.send(
                                f"GG! {player1.mention} chose {player1_choice.content}, which broke {player2.mention}'s {player2_choice.content}"
                            )
                        if player2_choice.content == "paper":
                            await ctx.send(
                                f"GG! {player2.mention} chose {player2_choice.content}, which wrapped itself and defeated {player1.mention}'s {player1_choice.content}"
                            )
                    if player1_choice.content == "paper":
                        if player2_choice.content == "scissors":
                            await ctx.send(
                                f"GG! {player2.mention}'s {player2_choice.content} cut {player1.mention}'s {player1_choice.content}!"
                            )
                        elif player2_choice.content == "stone":
                            await ctx.send(
                                f"GG! {player2.mention} chose {player2_choice.content}, which wrapped itself and defeated {player1.mention}'s {player1_choice.content}"
                            )
                    elif player1_choice.content == "scissors":
                        if player2_choice.content == "stone":
                            await ctx.send(
                                f"GG! {player2.mention} chose {player2_choice.content}, which CRUSHED {player1.mention}'s {player1_choice.content}"
                            )
                        elif player2_choice.content == "paper":
                            await ctx.send(
                                f"GG! {player1.mention} chose scissors which cut up {player2.mention}'s papers!"
                            )


@client.command()
async def timer(ctx, *, seconds, reason=None):
    try:
        secondint = int(seconds)
        if secondint > 300:
            await ctx.send(
                "I dont think im allowed to do go above 300 seconds.")
            raise BaseException
        if secondint < 0 or secondint == 0:
            await ctx.send("I dont think im allowed to do negatives")
            raise BaseException
        message = await ctx.send(
            f"   🕒   {ctx.author.mention}, Your Timer Named {reason} has been  Set For {seconds} seconds"
        )
        while True:
            secondint = secondint - 1
            if secondint == 0:
                await message.edit(new_content=("Ended!"))
                break
            await message.edit(new_content=("Timer: {0}".format(secondint)))
            await asyncio.sleep(1)
        await ctx.send(ctx.message.author.mention +
                       f"Your countdown for {seconds} Has ended!")
    except ValueError:
        await ctx.send("Must be a number!")


@client.command(pass_context=True)
async def broadcast(ctx, *, msg):
    for server in client.servers:
        for channel in server.channels:
            try:
                await client.send_message(channel, msg)
            except Exception:
                continue
            else:
                break


@client.command(aliases=["ty", "thank"])
async def thankyou(
        ctx,
        member: discord.Member,
):

    if not member:  # if member is no mentioned
        await ctx.send("User isnt Mentioned  :grey_question:")

    embed = discord.Embed(
        title=f"Thank you** {member.name}** from {ctx.author.name}. T",
        description=':kissing_heart: :partying_face:',
        color=0xea7938)
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/772665263463464970/795688394909941770/giphy.gif'
    )
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')(
            text=f"Sent by {ctx.author} from {ctx.guild}",
            icon_url=ctx.author.avatar_url)
    await member.send(embed=embed)
    await ctx.send(f'Your thanks has been sent to{member.mention}')


@client.command(aliases=["wc", "welcs"])
async def welcome(
        ctx,
        member: discord.Member,
):

    if not member:  # if member is no mentioned
        await ctx.send("User isnt Mentioned  :grey_question:")

    embed = discord.Embed(
        title=f"Welcome** {member.name}** To {ctx.guild.name}.",
        description=':kissing_heart: :partying_face:',
        color=0xea7938)
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/771998022807584797/798781439864864768/unnamed.gif'
    )
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    await ctx.send(embed=embed)


@client.command()
async def website(ctx):
    embed = discord.Embed(
        title=f"**RKS NOW HAS A WEBSITE** \n {ctx.author} did you check it?",
        colour=discord.Colour.blue())

    embed.add_field(
        name="[click here for the website](https://rksbot.netlify.app/)",
        value=
        "After almost a year of RKS, AramanSri has launched the official RKS Website for all your needs and info. Check it out now",
        inline=False)
    embed.set_image(
        url=
        'https://cdn.discordapp.com/attachments/772665263463464970/793452624909303818/rksbot.netlify.app.png'
    )
    await ctx.send(embed=embed)


@client.command(aliases=["userinfo", "aboutuser"])
async def whois(ctx, member: discord.Member = None):
    user = ctx.author if not member else member
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="ID:", value=user.id)
    embed.add_field(name="Display Name:", value=user.display_name)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user) + 1))
    embed.add_field(
        name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(
            name="Roles [{}]".format(len(user.roles) - 1),
            value=role_string,
            inline=False)

    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    return await ctx.send(embed=embed)


@client.command(aliases=["avatar"])
async def pfp(ctx, member: discord.Member):
    embed = discord.Embed(title=f"{member.name}'s avatar")
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def poll(ctx, ch: discord.TextChannel = None):
    if ch == None:
        await ctx.send('Channel not specified')
        return

    def check(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel

    await ctx.send('Enter the Poll title')
    t = await client.wait_for('message', check=check, timeout=60)
    await ctx.send('Enter the Poll Option 1')
    poll1 = await client.wait_for('message', check=check, timeout=120)
    await ctx.send('Enter the Poll Option 2')
    poll2 = await client.wait_for('message', check=check, timeout=120)
    embed = discord.Embed(
        title=t.content,
        description=f"1️⃣ {poll1.content} \n\n 2️⃣  {poll2.content}",
        color=0xffff)
    embed.set_footer(
        icon_url=
        'https://cdn.discordapp.com/attachments/772665263463464970/801704591058010152/R.gif',
        text='Bot ID:760415780176658442 , Bot Name: RKS')
    poll1 = await ch.send(embed=embed)
    await poll1.add_reaction('1️⃣')
    await poll1.add_reaction('2️⃣')


@client.command()
async def sinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    guild = ctx.guild
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    total_text_channels = len(guild.text_channels)
    total_voice_channels = len(guild.voice_channels)
    total_channels = total_text_channels + total_voice_channels
    role_count = len(ctx.guild.roles)
    list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
    staff_roles = [
        "Owner", "Head Dev", "Dev", "Head Admin", "Admins", "Moderators",
        "Community Helpers", "Members"
    ]

    embed2 = discord.Embed(
        timestamp=ctx.message.created_at, color=ctx.author.color)
    embed2.add_field(name='Name', value=f"{ctx.guild.name}", inline=True)
    embed2.add_field(name='Owner', value=f"{ctx.guild.owner}", inline=True)
    embed2.add_field(
        name='Verification Level',
        value=str(ctx.guild.verification_level),
        inline=True)
    embed2.add_field(
        name='Highest role', value=ctx.guild.roles[-2], inline=True)
    embed2.add_field(name='Contributers:', value="None")
    embed2.add_field(name="Server ID", value=id, inline=True)
    embed2.add_field(name="Region", value=region, inline=True)
    embed2.add_field(
        name="Server Channels: ", value=total_channels, inline=True)
    embed2.add_field(
        name="Server Text Channels: ", value=total_text_channels, inline=True)
    embed2.add_field(
        name="Server Voice Channels: ",
        value=total_voice_channels,
        inline=True)

    for r in staff_roles:
        role = discord.utils.get(ctx.guild.roles, name=r)
        if role:
            members = '\n'.join([member.name
                                 for member in role.members]) or "None"
            embed2.add_field(name=role.name, value=members)

    embed2.add_field(
        name='Number of roles', value=str(role_count), inline=True)
    embed2.add_field(
        name='Number Of Members', value=ctx.guild.member_count, inline=True)
    embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed2.add_field(
        name='Created At',
        value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),
        inline=True)
    embed2.set_thumbnail(url=ctx.guild.icon_url)
    embed2.set_author(name=f"{ctx.guild.name} Information")

    await ctx.send(embed=embed2)

@client.command(aliases=['lvl', 'rank'])
@cooldown(1, 5, BucketType.member)
async def level(ctx, member: discord.Member = None):
	if member == None:
		member = ctx.author
	with open('./Data/levels.json', 'r', encoding='utf8') as f:
		user = json.load(f)
	guild = user[str(ctx.guild.id)]
	level = user[str(ctx.guild.id)][str(member.id)]['level']
	ranks = []
	rank = 1
	lvl = user[str(ctx.guild.id)][str(member.id)]['level']  + 1
	exps=[60]
	if lvl == 696969696969696969696970:
		return
	while lvl > len(exps):
		exps.append(int(exps[-1] + exps[-1]/10))
		if lvl == len(exps):
			break
	lvl_end = exps[-1]
	for i in guild:
		if i.isdigit():
			if i == "774136203548557333":
				pass
			else:
				l = guild[str(i)]['level']
				ranks.append(l)
	ranks = sorted(ranks, reverse=True)
	for q in ranks:
		if q == level:
			break
		rank += 1

	if str(member.id) in guild:
		lvl = user[str(ctx.guild.id)][str(member.id)]['level']
		exp = user[str(ctx.guild.id)][str(member.id)]['exp']
	else:
		lvl = 0
		exp = 0
		lvl_end = 0
	if lvl == 0:
		rank = 0
		
	avatar = member.avatar_url_as(size=128)
	Level = lvl
	exp = exp
	exp_limit = lvl_end
	rank = rank
	name = member
	
	##

	Template = Image.open("./Images/Rank_card_template/Template.png")
	Full_bar = Image.open("./Images/Rank_card_template/Full_bar.png")
	R_bar  = Image.open("./Images/Rank_card_template/R_bar.png")
	mask  = Image.open("./Images/Rank_card_template/mask.png")
	font1 = ImageFont.truetype("./Fonts/Prototype.ttf", 30)
	font2 = ImageFont.truetype("./Fonts/Prototype.ttf", 35)

	draw = ImageDraw.Draw(Template)

	#Avatar Icon
	avatar_data = BytesIO(await avatar.read())
	pfp = Image.open(avatar_data)
	pfp.thumbnail((100,100))
	try:	
		Template.paste(pfp, (10,10) , pfp)
	except:
		Template.paste(pfp, (10,10))
	Template.paste(mask, (10,10), mask)

	#Name
	Name_text = unidecode(str(name))
	draw.text((120,30),Name_text,(225,225,225),font=font2)

	#Level
	Level_text = "Level:" + str(Level)
	draw.text((120,80),Level_text,(225,225,225),font=font1)

	#Exp
	Exp_text = "Exp:" + str(round(exp/100 , 1)) + "K/" + str(round(exp_limit/100 , 1))  + "K"
	draw.text((320,80),Exp_text,(225,225,225),font=font1)

	#Rank
	Rank_card_templateext = "Rank:" + str(rank)
	draw.text((520,80),Rank_card_templateext,(225,225,225),font=font1)

	#Exp Progress Bar
	exp_per = int((exp/exp_limit)*100)
	R_bar_position = 28
	if exp_per != 0 :
			bar_width = int(638*(exp_per/100))
			R_bar_position += bar_width
			Full_bar = ImageOps.fit(Full_bar, (bar_width,35))
			Template.paste(Full_bar, (28, 142), Full_bar)
	Template.paste(R_bar, (R_bar_position, 142), R_bar)

	Template.save( f"./Images/Output/{ctx.author.id}.png", "png" )

	await ctx.send(file = discord.File(f"./Images/Output/{ctx.author.id}.png"))


@level.error
async def level_error(ctx, error):
	if isinstance(error, CommandOnCooldown):
		msg = 'please try again in **`{:.2f} s`**'.format(error.retry_after)
		await ctx.send(
		    f'{ctx.author.mention} Please don\'t spam the chat, {msg}')
	else:
		ctx.command.reset_cooldown(ctx)
		raise error

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))
