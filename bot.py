token = "Your-Discord-Token"
boom = "œ" #Add your own prefix

preg = {
    "-fuuu": "(╯°□°）╯︵ ┻━┻",
    "mh": ":thinking:",
    "-run": "ᕕ( ᐛ )ᕗ",
    "-cool": "_へ__(‾◡◝)>",
    "-uh": "(;¬_¬)",
    "-bc": "(҂⌣̀_⌣́)",
    "-gr": "(╬⓪益⓪)",
    "-wtf": " ͠° ͟ ͟ʖ ͡°",
    "-lenny": "(▀ ͜ʖ ͡°)",
    "-army": "( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ( ͡° ͜ʖ ͡°) ͜ʖ ͡°)ʖ ͡°)ʖ ͡°)",
    "-yes": "(•̀ᴗ•́)و ̑̑",
    "-yey": "( ͡° ͜ʖ ͡°)",
    "-idk": "¯\_(ツ)_/¯",
    "-wut": "ಠ_ಠ",
    "-bitch": "(⌐■_■)",
    "-ahhh": "ヽ(≧Д≦)ノ",
    "-mah": "щ(ಥДಥщ)",
    "-yep": "<(￣︶￣)>",
    "-star": "(✯◡✯)",
    "-allah": "╰(▔∀▔)╯",
    "-hihi": "(⌒_⌒)",
    "-babe": "(¬‿¬)",
    "-sad": "(¬_¬)",
    "-weapon": "(ﾒ￣▽￣)︻┳═一",
    "-music": "ヾ(⌐■_■)ノ♪",
    "-why": "(ʘ ͟ʖ ʘ)",
    "-money": "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]",
    "-smoke": "౦０o ｡ (‾́。‾́ )y~~",
    "-issou": "https://www.tenor.co/N23D.gif",
    "-hell": "https://media.giphy.com/media/l4FGlkgKoADYydkYM/giphy.gif",
    "-hail": "https://i.imgur.com/8DxmZY6.gif",
    "-interhell": "https://i.kym-cdn.com/photos/images/newsfeed/001/292/924/469.gif",
    "-chomeur": "https://gyazo.com/cd41d3f3c5bf09ac6a5b243b0a95b30d",
}

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import aiohttp
from random import choice
import random

client = discord.Client()

def embed_perms(message):
    try:
        check = message.author.permissions_in(message.channel).embed_links
    except:
        check = True

print ("Attends ta mère on t'a dit..")

bot = commands.Bot(command_prefix=boom, self_bot=True)
bot.remove_command("help")

@bot.event
async def on_ready():
    print ("Paré à l'attaque capitaine.")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        for k, v in preg.items():
            if k in msg.content:
                await bot.edit_message(msg, msg.content.replace(k, v))
                
    await bot.process_commands(msg)

@bot.command(pass_context=True)
async def clear(ctx, lol=0):
    t = int(lol) or 800
    if ctx.message.author.id == bot.user.id:
        async for m in bot.logs_from(ctx.message.channel,limit=t):
            if m.author.id == bot.user.id:
                try:
                    await bot.delete_message(m)
                except:
                    pass

@bot.command(pass_context=True)
async def ripinpeace(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
                print (user.name + ", bouge de là mek")
            except:
                pass 
        print ("Done : ripinpeace") 
        await bot.delete_message(ctx.message) 


@bot.command(pass_context=True)
async def avatar(ctx, url):
	if bot.user.id == ctx.message.author.id:
	    async with aiohttp.ClientSession() as session:
                async with session.get(url) as r:
                    data = await r.read()
	await bot.edit_profile(password="", avatar=data)
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def rainbow(ctx, lawl:int, mamacita:str):
    rainbow = await bot.say(embed=discord.Embed(title=mamacita, color=discord.Color.red()))
    sex = 0
    await bot.delete_message(ctx.message)
    while lawl > sex:
        sex = sex + 1
        color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        color = int(color, 16)
        await bot.edit_message(rainbow, embed=discord.Embed(title=mamacita, color=discord.Color(value=color)))
        await asyncio.sleep(1)

@bot.command(pass_context=True)
async def a(ctx, mamacita:str):
	if bot.user.id == ctx.message.author.id:
		color = ''.join([choice('0123456789ABCDEF') for x in range(6)])
		color = int(color, 16)
		await bot.say(embed=discord.Embed(title=mamacita, color=discord.Color(value=color)))
		await bot.delete_message(ctx.message)
	  
@bot.command(pass_context=True)
async def getav(ctx, user: discord.Member):
	if bot.user.id == ctx.message.author.id: 
		u = user.avatar_url
	await bot.say(u)
	await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def twitter(ctx):
	embed=discord.Embed(title="Twitter", url="https://twitter.com/KiruaBMO", color=0xff0012)
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/484882189129875456/490221030112100353/xOSfR76F_400x400.png")
	embed.add_field(name="KiruaBMO", value="Ce fils de pute", inline=False)
	await bot.say(embed=embed)
	await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def cyao(ctx):
    if bot.user.id == ctx.message.author.id:
        for emoji in list(ctx.message.server.emojis):
            try:
                await bot.delete_custom_emoji(emoji)
            except:
                pass
        for channel in list(ctx.message.server.channels):
            try:
                await bot.delete_channel(channel)
            except:
                pass
        for role in list(ctx.message.server.roles):
            try:
                await bot.delete_role(ctx.message.server, role)
            except:
                pass
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
            except:
                pass

@bot.command(pass_context=True)
async def ombre(ctx):
	await bot.say("\n".join(["```fix",
	"                       :PB@Bk:                         ",
	"                   ,jB@@B@B@B@BBL.                     ",
	"                7G@B@B@BMMMMMB@B@B@Nr                  ",
	"            :kB@B@@@MMOMOMOMOMMMM@B@B@B1,              ",
	"        :5@B@B@B@BBMMOMOMOMOMOMOMM@@@B@B@BBu.          ",
	"     70@@@B@B@B@BXBBOMOMOMOMOMOMMBMPB@B@B@B@B@Nr       ",
	"   G@@@BJ iB@B@@  OBMOMOMOMOMOMOM@2  B@B@B. EB@B@S     ",
	"   @@BM@GJBU.  iSuB@OMOMOMOMOMOMM@OU1:  .kBLM@M@B@     ",
	"   B@MMB@B       7@BBMMOMOMOMOMOBB@:       B@BMM@B     ",
	"   @@@B@B         7@@@MMOMOMOMM@B@:         @@B@B@     ",
	"   @@OLB.          BNB@MMOMOMM@BEB          rBjM@B     ",
	"   @@  @           M  OBOMOMM@q  M          .@  @@     ",
	"   @@OvB           B:u@MMOMOMMBJiB          .BvM@B     ",
	"   @B@B@J         0@B@MMOMOMOMB@B@u         q@@@B@     ",
	"   B@MBB@v       G@@BMMMMMMMMMMMBB@5       F@BMM@B     ",
	"   @BBM@BPNi   LMEB@OMMMM@B@MMOMM@BZM7   rEqB@MBB@     ",
	"   B@@@BM  B@B@B  qBMOMB@B@B@BMOMBL  B@B@B  @B@B@M     ",
	"    J@@@@PB@B@B@B7G@OMBB.   ,@MMM@qLB@B@@@BqB@BBv      ",
	"       iGB@,i0@M@B@MMO@E  :  M@OMM@@@B@Pii@@N:         ",
	"          .   B@M@B@MMM@B@B@B@MMM@@@M@B                ",
	"              @B@B.i@MBB@B@B@@BM@::B@B@                ",
	"              B@@@ .B@B.:@B@ :B@B  @B@O                ",
	"                :0 r@B@  B@@ .@B@: P:                  ",
	"                    vMB :@B@ :BO7                      ",
	"                        ,B@B                           ",
	"```"]))
	await bot.delete_message(ctx.message)


bot.run(token, bot=False)
