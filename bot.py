import discord
from discord.ext import commands




client = commands.Bot(command_prefix='!')


@client.event
async def on_message(message):
    if message.author.bot == True:
        return
    if message.channel.name != 'general':
        return

    if len(message.attachments) != 0:
        for attatch in message.attachments:
            await attatch.save('downloads/{}.png'.format(attatch.id))
            with open('downloads/{}.png'.format(attatch.id), 'rb') as fp:
                await message.channel.send(file=discord.File(fp, '{}.png'.format(attatch.id)))
    if message.content != '':
           await message.channel.send(message.content)
    await message.delete()


client.run("NzE5MTAyOTgzNDI1NDkwOTk0.XvTqiw.UgCYNRGgOPHcN_SLjChaW2BDRi4")