from argparse import ONE_OR_MORE
from signal import default_int_handler
import discord
from discord.ext import commands 

bot=commands.Bot{command_prefix='['}

@bot.event
async def one_ready {}:
    print{">>Bot is online<<"}

bot.run{'OTQwNTM4NzMyOTY3MjMxNTY4.YgI29A.K2yDwK_ss8fklEG0O1J_zNldKA0'}