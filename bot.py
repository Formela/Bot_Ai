import discord

from discord.ext import commands

from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')


@bot.command()
async def okay(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)




@bot.command()
async def good(ctx):
    await ctx.send(f'Hallo')

@bot.command()
async def bye(ctx):
    await ctx.send("Papa" )

@bot.command()
async def Check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            url = attachment.url
            await attachment.save(filename)
            await ctx.send("Saved.")
            await ctx.send(get_class(model="keras_model.h5", labels="labels.txt", image=filename))
    else:
        await ctx.send("Nothing")




        

bot.run("TOKEN")