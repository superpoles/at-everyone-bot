import logging
logging.basicConfig(level=logging.INFO)

import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='$$$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')

@bot.event
async def on_message(message):
    if message.mention_everyone == True:
        await message.channel.send('fuck you.')
    if '<:dab:299028890180124672>' in message.content:
        await message.channel.send('fuck you dont dab in chat')
    if message.author.id == 171783855735308288:
        emoji = <:jonx:453310199558832140>
        await message.add_reaction(emoji)
    

#useless for now
#@bot.event
#async def on_reaction_add(reaction, user):
#    message = reaction.message
#    print(reaction.emoji)
#    if reaction.count >= 3:
#        if reaction.emoji == "👢":
#            await Guild.kick(member, reason="3 boots")

@bot.event
async def on_member_remove(member):
    print(member.nick+"out, cya")
    

bot.run('...')
