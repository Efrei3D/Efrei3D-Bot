import discord
from discord.ext import commands, tasks
import json
import os
from itertools import cycle
from helloasso_pyapi.main_helloasso import run_api
import asyncio

token = 'MTAwOTAyODc0NTYwMjAwNzA3MA.GjB1xb.E0F9C3NRad3969BmUr8e87gjEdllVzbI72fQBA'
prefix = '!'

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

# Intents
intents = discord.Intents.all()
intents.message_content = True
# The bot
bot = commands.Bot(command_prefix=prefix, description="Hello there! I'm Efrei3D Bot.", intents = intents)



# # Load Cogs
# async def main():
#     async with bot:
#         for filename in os.listdir("Cogs"):
#             if filename.endswith(".py"):
#                 await bot.load_extension(f"Cogs.{filename[:-3]}")
#                 # await bot.start(token)

@bot.event
async def on_ready():
    print(f"{bot.user} is now running")
    print(f"Discord version: {discord.__version__}")
    print(f"Bot version: b0.5")
    activity_watching = discord.Activity(type=discord.ActivityType.watching, name = f"Blender Tutorials")
    await bot.change_presence(status = discord.Status.online, activity = activity_watching)
    run_api()

@bot.command(name = "stop",
                    usage = '',
                    description = "shutsdown the bot",
                    aliases = ['sd'])
async def stop_cmd(ctx):
    await ctx.send("https://tenor.com/view/star-wars-darth-vader-noo-no-gif-15893771")
    exit()

@bot.command(name = "give_role",
                        usage = '',
                        description = "give roles to new members")
async def give_role(ctx):
    with open("short_memberlist.json", 'r') as f: memberlist = json.load(f)
    for element in memberlist:
        user_data, user_dscd = memberlist[element], memberlist[element]["discord"]
        converter = commands.MemberConverter()
        user_dscd = await converter.convert(ctx, user_dscd)
        await user_dscd.add_roles(discord.utils.get(user_dscd.guild.roles, name = "Membre 2022-2023"))
        print(f'role given to {user_data["firstname"]} {user_data["lastname"]}')
        await user_dscd.edit(nick=f'{user_data["firstname"]} {user_data["lastname"]}')
        print(f'{user_dscd} nick was changed to \"{user_data["firstname"]} {user_data["lastname"]}\"\n\n')
    await ctx.send("all new users roles and nicks were updated")
    print("all new users roles and nicks were updated")

if __name__ == "__main__":
    # asyncio.run(main())
    # main()
    bot.run(token)