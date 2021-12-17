from functools import _Descriptor
import discord
from discord import member
from discord import guild
from discord.activity import Game
from discord.ext import commands
from discord.ext.commands import has_permissions

#prefix bota

client = commands.Bot(command_prefix="+")
client.remove_command("help")

#konsola bota

@client.event
async def on_ready():
    print("Bot włączony!")
    await client.change_presence(activity=discord.Game(name="+help"))

#komenda help

@client.command()
async def help(ctx):

   embed=discord.Embed(title="Help Commands", color=0x092fec)
   embed.set_author(name="Toxic_Bot")
   embed.add_field(name="Help_command", value="Pokazuje komendy", inline=True)
   embed.add_field(name="Help_admin", value="Pokazuje komendy administracyjne", inline=True)
   embed.add_field(name="Help_vip", value="Jak mogę dostać vipa?", inline=True)
   await ctx.send(embed=embed)

#komenda Help_commands

@client.command()
async def Help_commands(ctx):
    embed=discord.Embed(title="Help Commands:", color=0x092fec)
    embed.set_author(name="Toxic_Bot")
    embed.add_field(name="!d bump - ", value="Podbija server na liście", inline=False)
    embed.add_field(name="&rank - ", value="Pokazuje twój aktualny level", inline=False)
    embed.add_field(name="&top - ", value="Pokazuje topke w śród użytkowników", inline=True)
    await ctx.send(embed=embed)


#komenda Help_admin

@client.command()
async def Help_admin(ctx):
    embed=discord.Embed(title="Help Commands:", color=0xff0000)
    embed.set_author(name="Toxic_Bot")
    embed.add_field(name="&ban -", value="(blokuje członka)", inline=False)
    embed.add_field(name="&unban  -", value="(odblokowuje członka)", inline=False)
    embed.add_field(name="&kick", value="(wyrzuca członka)", inline=False)
    embed.add_field(name="&vkick", value="(wyrzuca członka z kanału głosowego)", inline=False)
    embed.add_field(name="&mute", value="(wycisz członka na kanałach tekstowych, uniemożliwiając mu pisanie)  (czas dopóki ktoś z administracji nie od ciszy!)", inline=False)
    embed.add_field(name="&unmute ", value="(dezaktywuje wyciszenie członka)", inline=False)
    embed.add_field(name="&vmute", value="(wycisza członka na kanałach głosowych, aby nie mógł mówić)  (czas dopóki ktoś z administracji nie od ciszy!)", inline=False)
    embed.add_field(name="&unvmute", value="(usuwa wyciszenie członka na kanałach głosowych)", inline=False)
    embed.add_field(name="&clear", value="(usuwa wiadomości na kanale tekstowym)", inline=False)
    embed.add_field(name="&warn", value="(ostrzega, daje upomnienie członkowi)", inline=False)
    embed.add_field(name="&removewarn", value="(usuń ostrzeżenia dla użytkownika)", inline=False)
    embed.add_field(name="&setnick", value="(zmienia pseudonim członka)", inline=False)
    embed.add_field(name="Komenda na zrobienie konkursu", value=" !gstart (liczba dni np. 14d) (tytuł konkursu np. ranga VIP) ", inline=False)
    embed.add_field(name="Na przykład", value="!gstart 14d ranga VIP", inline=False)
    await ctx.send(embed=embed)


#komenda Help_vip

@client.command()
async def Help_vip(ctx):
    embed=discord.Embed(title="Help Commands:", color=0xfff700)
    embed.set_author(name="Toxic_Bot")
    embed.add_field(name="Vip", value="Vipa odblokujesz po wbiciu 60 lvl lub za opłatą 5 zł", inline=False)
    embed.add_field(name="Svip", value="Svipa odblokujesz po wbiciu 70 lvl lub za opłatą 10 zł", inline=False)
    embed.add_field(name="Co daje vip?", value="Po otrzymaniu rangi vip lub svip dostajesz możliwość pisania na ukrytych kanałach oraz darmowe gry typu: cyberpunk 2077, forza horizon 5 premium", inline=True)
    await ctx.send(embed=embed)


#komendy administracyjne

#Komenda ban

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.ban(reason=reason)
    await ctx.channel.send("Zbanowano użytkownika {member.mention} za {reason}")

#Komenda kick

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason="Bez Powodu"):
    await member.kick(reason=reason)
    await ctx.channel.send("Wyrzucono użytkownika {member.mention} za {reason}")

#komenda mute

@client.command(Descriptor="Wycisza określonego użytkownika.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, reason="Bez Powodu"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_message=False, read_message_history=False, read_message=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send("Wyciszono użytkownika {member.mention} za {reason}")
    await member.send("Zostałeś/aś wyciszony/ona na serverze {guild.name} za {reason}")


client.run("OTIxNDU5NTM4OTIwNjM2NDY3.YbzOEQ.Qt95RMp4tz4jaJT3cL9Q_kUEs34")