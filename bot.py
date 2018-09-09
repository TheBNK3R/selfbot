token = "Your-Discord-Token"
boom = "œ" #Add your own prefix

preg = {
    "-fuuu": "(╯°□°）╯︵ ┻━┻",
    "mh": ":thinking:",
    "-run": "ᕕ( ᐛ )ᕗ",
    "-cool": "_へ__(‾◡◝ )>",
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
}

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

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
                await bot.delete_message(m)

@bot.command(pass_context=True)
async def ripinpeace(ctx):
    if bot.user.id == ctx.message.author.id:
        for user in list(ctx.message.server.members):
            try:
                await bot.ban(user)
                print (user.name + ", bouge de là mek")
            except:
                pass 
        print ("Done, rip")  

bot.run(token, bot=False)
