#ссылка на бота:https://discord.com/oauth2/authorize?client_id=1231177142109212682&permissions=8&scope=bot
import config, discord
from discord.ext import commands
from model import *

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='.', description=description, intents=intents)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for i in ctx.message.attachments:
            file_name=i.filename
            file_url=i.url
            await i.save(f'images/{i.filename}')
            await ctx.send(f'Мы сохранили файл{i.filename}')
            name, procent = detect_bird(img=f'images/{i.filename}', model='pet_progect-main\keras_model.h5', label='pet_progect-main\labels.txt')
            await ctx.send(name)
    else:
        await ctx.send("У вас нет фото :(")

bot.run(config.token)