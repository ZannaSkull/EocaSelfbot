# Reversed By Hisako🎀#2004 
import discord
from discord.ext import commands
import os, colorama
from colorama import Fore, Back, Style, init
import cursor, msvcrt, requests
cursor.hide()
from pwinput import pwinput
import time, nacl, webbrowser, threading, re
init(convert=True)
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=(open('data/prefix.txt', 'r').read()), intents=intents, self_bot=True)
bot.remove_command('help')
eoca = f"{Fore.LIGHTMAGENTA_EX}┌─┐┌─┐┌─┐┌─┐  ┌─┐┌─┐┬  ┌─┐┌┐ ┌─┐┌┬┐\n├┤ │ ││  ├─┤  └─┐├┤ │  ├┤ ├┴┐│ │ │ \n└─┘└─┘└─┘┴ ┴  └─┘└─┘┴─┘└  └─┘└─┘ ┴ "

@bot.event
async def on_ready():
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


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    current_autoreply = open('data/autoreply.txt', 'r').read()
    autoreply_mode = open('data/autoreplymode.txt', 'r').read()
    autoreply_trigger = open('data/autoreplytrigger.txt', 'r').read()
    autoreply_case = open('data/autoreplycasesensitive.txt', 'r').read()
    autoreply_state = open('data/autoreply_state.txt', 'r').read()
    if autoreply_state == 'enabled':
        if message.author != bot.user:
            if autoreply_mode == 'exact':
                if autoreply_case == 'true':
                    if message.content == autoreply_trigger:
                        await message.channel.send(current_autoreply)
                        try:
                            print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in "{Fore.LIGHTWHITE_EX}{message.guild.name}{Fore.LIGHTMAGENTA_EX}" with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')
                        except:
                            print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in {Fore.LIGHTWHITE_EX}a non-guild domain{Fore.LIGHTMAGENTA_EX} with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')

                else:
                    pass
                if message.content.lower() == autoreply_trigger.lower():
                    await message.channel.send(current_autoreply)
                    try:
                        print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in "{Fore.LIGHTWHITE_EX}{message.guild.name}{Fore.LIGHTMAGENTA_EX}" with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')
                    except:
                        print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in {Fore.LIGHTWHITE_EX}a non-guild domain{Fore.LIGHTMAGENTA_EX} with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')

                    if autoreply_mode == 'within':
                        if autoreply_case == 'true':
                            if findWholeWord(autoreply_trigger)(message.content):
                                await message.channel.send(current_autoreply)
                                try:
                                    print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in "{Fore.LIGHTWHITE_EX}{message.guild.name}{Fore.LIGHTMAGENTA_EX}" with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')
                                except:
                                    print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in {Fore.LIGHTWHITE_EX}a non-guild domain{Fore.LIGHTMAGENTA_EX} with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')

                        else:
                            if findWholeWord(autoreply_trigger.lower())(message.content.lower()):
                                await message.channel.send(current_autoreply)
                                try:
                                    print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in "{Fore.LIGHTWHITE_EX}{message.guild.name}{Fore.LIGHTMAGENTA_EX}" with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')
                                except:
                                    print(f'successfully replied to "{Fore.LIGHTWHITE_EX}{message.content}{Fore.LIGHTMAGENTA_EX}" by {Fore.LIGHTWHITE_EX}{message.author.name}#{message.author.discriminator}{Fore.LIGHTMAGENTA_EX} in {Fore.LIGHTWHITE_EX}a non-guild domain{Fore.LIGHTMAGENTA_EX} with "{Fore.LIGHTWHITE_EX}{current_autoreply}{Fore.LIGHTMAGENTA_EX}"!')


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
while 1:
    os.system('cls')
    os.system('mode 45,9')
    os.system(f"title eoca selfbot V{version} ~ hub")
    print(f"{Fore.LIGHTMAGENTA_EX}{eoca}\n")
    print(f"{Fore.LIGHTWHITE_EX}1){Fore.LIGHTMAGENTA_EX} launch client!")
    print(f"{Fore.LIGHTWHITE_EX}2){Fore.LIGHTMAGENTA_EX} list of commands!")
    print(f"{Fore.LIGHTWHITE_EX}3){Fore.LIGHTMAGENTA_EX} change settings!")
    print(f"{Fore.LIGHTWHITE_EX}4){Fore.LIGHTMAGENTA_EX} direct support!")
    inp = msvcrt.getch()
    inp = str(inp)[2]
    if inp == '2':
        total_commands = 12
        os.system('cls')
        os.system(f"mode 66,{total_commands + 5}")
        os.system(f"title eoca selfbot V{version} ~ commands")
        amount_of_commands = 1
        print(eoca + '\n')
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}presence ({Fore.LIGHTWHITE_EX}playing/listening/watching{Fore.LIGHTMAGENTA_EX}) ({Fore.LIGHTWHITE_EX}phrase{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}stream ({Fore.LIGHTWHITE_EX}streamer_username{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}spamthis ({Fore.LIGHTWHITE_EX}your_message{Fore.LIGHTMAGENTA_EX}) ({Fore.LIGHTWHITE_EX}amount{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}spamimage ({Fore.LIGHTWHITE_EX}image_name.png{Fore.LIGHTMAGENTA_EX}) ({Fore.LIGHTWHITE_EX}amount{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}massping ({Fore.LIGHTWHITE_EX}amount{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}massdelete ({Fore.LIGHTWHITE_EX}amount{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}nuke ({Fore.LIGHTWHITE_EX}phrase{Fore.LIGHTMAGENTA_EX}) ({Fore.LIGHTWHITE_EX}image_name.png{Fore.LIGHTMAGENTA_EX}) ({Fore.LIGHTWHITE_EX}amount{Fore.LIGHTMAGENTA_EX}) ({Fore.LIGHTWHITE_EX}kick/ban/none{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}status ({Fore.LIGHTWHITE_EX}@user#0001{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}getavatar ({Fore.LIGHTWHITE_EX}@user#0001{Fore.LIGHTMAGENTA_EX})")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}members")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}membercount")
        amount_of_commands += 1
        print(f"{Fore.LIGHTWHITE_EX}{str(amount_of_commands)}) {Fore.LIGHTMAGENTA_EX}clearlogs")
        os.system('pause>nul')
    if inp == '1':
        os.system('start client.exe')
    if inp == '4':
        os.system('cls')
        os.system('mode 45,6')
        os.system(f"title eoca selfbot V{version} ~ support")
        print(eoca + '\n\nloading...')
        try:
            username = 'eoca#0176'
            r = requests.get('https://lookupsocial.herokuapp.com/api/user/profile?q730169105176592426')
            data = r.json()
            username = data['data']['username']
        except:
            pass

        os.system('cls')
        os.system('mode 54,8')
        os.system(f"title eoca selfbot V{version} ~ support")
        print(eoca + '\n')
        print(f"eoca's discord server: {Fore.LIGHTWHITE_EX}https://discord.gg/5tBcpzh22H")
        print(f"{Fore.LIGHTMAGENTA_EX}eoca's discord: {Fore.LIGHTWHITE_EX}{username}")
        print(f"{Fore.LIGHTMAGENTA_EX}eoca's discord id: {Fore.LIGHTWHITE_EX}730169105176592426{Fore.LIGHTMAGENTA_EX}")
        os.system('pause>nul')
    if inp == '3':
        done = False
        while done == False:
            os.system('cls')
            os.system('mode 45,8')
            os.system(f"title eoca selfbot V{version} ~ settings")
            print(eoca + '\n')
            current_prefix = open('data/prefix.txt', 'r').read()
            print(f"{Fore.LIGHTWHITE_EX}1) {Fore.LIGHTMAGENTA_EX}prefix: {Fore.LIGHTWHITE_EX}{current_prefix}{Fore.LIGHTMAGENTA_EX}")
            print(f"\npress {Fore.LIGHTWHITE_EX}`{Fore.LIGHTMAGENTA_EX} to exit!")
            choice = msvcrt.getch()
            choice = str(choice)[2]
            if choice == '`':
                done = True
            if choice == '1':
                os.system('cls')
                os.system('mode 45,8')
                os.system(f"title eoca selfbot V{version} ~ settings")
                print(eoca + '\n')
                new_prefix = input(f"{Fore.LIGHTWHITE_EX}1) {Fore.LIGHTMAGENTA_EX}prefix: {Fore.LIGHTWHITE_EX}")
                with open('data/prefix.txt', 'r+') as f:
                    f.truncate(0)
                f = open('data/prefix.txt', 'a')
                f.write(new_prefix)
                f.close()
                bot = commands.Bot(command_prefix=(open('data/prefix.txt', 'r').read()), self_bot=True)