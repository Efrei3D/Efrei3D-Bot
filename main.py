from pydoc import describe
import discord
from discord.ext import commands, tasks
import os, platform, json
from itertools import cycle
from helloasso_pyapi.main_helloasso import run_api
import asyncio

with open("discord_secrets.json", 'r') as f: secrets = json.load(f)
token = secrets["token"]
prefix = '!'

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

# Intents
intents = discord.Intents.all()
intents.message_content = True
# The bot
bot = commands.Bot(command_prefix=prefix,
                    owner_id = 315927396081729536,
                    help_command=None,
                    description="Hello there! I'm Efrei3D Bot.",
                    intents = intents)


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
    print(f"Bot version: b0.7.1")
    activity_watching = discord.Activity(type=discord.ActivityType.watching, name = f"Blender Tutorials")
    # activity_watching = discord.CustomActivity(name = f"This is a custom activity 🦖", type=discord.ActivityType.custom, emoji=None)
    await bot.change_presence(status = discord.Status.online, activity = activity_watching)
    # run_api()

# gives answers and/or reactions to things the members say (ex: "Hello There", "Gros Cailloux", and so on)
@bot.event
async def on_message(msg):
    msg_l = str(msg.content).lower()
    chan_id = msg.channel.id
    id_list = [622172756686929930, 960123071337988126, 622175409215373323, 773453166687158286, 542435497281323008, 542435497281323008, 893186704977055746, 628917753482313758]
    if msg_l=="hello there" and chan_id not in id_list:
        await msg.channel.send('https://tenor.com/view/hello-there-general-kenobi-star-wars-grevious-gif-17774326')
    elif msg_l=="gros cailloux" or msg_l=="grocailloux": await msg.channel.send("https://cdn.discordapp.com/emojis/908083545791160361.webp?size=128&quality=lossless")
    else: await bot.process_commands(msg)


@bot.command(name="help",
            usage=f'{prefix}help',
            description='displays all commands available to you',
            aliases=['h'])
async def help_cmd(ctx):
    spacing = "\t ​ ​ ​ ​ ​ ​ ​ ​\t"
    embed=discord.Embed(title="**Tu cherches une commande ?**", description="prefix: !", color=0x7ec75b)
    embed.set_thumbnail(url="https://cdn.helloasso.com/img/logos/efrei%203d-8fe1b94ab4c44666ac64ffc89ae19641.png")
    
    embed.add_field(name="socials", value='Liste l\'ensemble des endroits où tu peux nous retrouver, sur le web et sur campus', inline=False)
    if ctx.message.author.guild_permissions.administrator == True:
        embed.add_field(name="give_role", value="Adds this year's member role to all new members, and nicks them (<firstname><lastname>)", inline=False)
    if ctx.message.author.id == 315927396081729536:
        embed.add_field(name="stop", value=f'Allows user to remotely shut down the bot', inline=False)
    embed.set_footer(text="Efrei3D: Parce que la réalité ne nous suffit pas 🦖")
    await ctx.send(embed=embed)


@bot.command(name = "stop",
                    usage = '',
                    description = "shutsdown the bot",
                    aliases = ['sd'])
@commands.is_owner()
async def stop_cmd(ctx):
    await ctx.send("https://tenor.com/view/star-wars-darth-vader-noo-no-gif-15893771")
    exit()


@bot.command(name = "Efrei 3D".lower(),
            usage = '',
            description = "Returns current information about the association",
            aliases = ["Efrei3D".lower()])
async def efrei3d(ctx):
    spacing = "\t ​ ​ ​ ​ ​ ​ ​ ​\t"
    embed=discord.Embed(title="**Qui sommes nous ?**", description="Efrei3D est une association créé le 27 mars 2009 qui tourne autour de la 3D. Qu'il s'agisse de modélisation (Blender, SolidWorks), d'impression 3D, de création de jeux vidéos (Unreal Engine) ou même de création de cours métrages, nous proposons de former et partager des connaissances autour de projets en tout genres.", color=0x7ec75b)
    embed.set_thumbnail(url="https://cdn.helloasso.com/img/logos/efrei%203d-8fe1b94ab4c44666ac64ffc89ae19641.png")
    embed.add_field(name="__Nos locaux__", value='Sur le campus République, 1er étage du bâtiment E, à côté des salles de réunion.')
    embed.add_field(name="\n__Le bureau restreint__", value=f'**Président :** Nathan Morel{spacing} ​ ​ **Vice-Président :** Victor Steimberg\n**Trésorier :** Constantin Dragan ​ ​ **Secrétaire :** Bastien Robert\n', inline=False)
    embed.add_field(name="__Le bureau étendu__", value=f'**Responsable Handicap :** Christian Miclea\n**Responsables Communication :**\nEyfeline Tala{spacing}Martin Kang{spacing}Samuel Poinama', inline=False)
    embed.set_footer(text="Efrei3D: Parce que la réalité ne nous suffit pas 🦖")
    await ctx.send(embed=embed)

@bot.command(name = "socials",
            usage = '',
            description = "gives a list of Efrei3D social networks")
async def give_socials(ctx):
    spacing = "\t ​ ​ ​ ​ ​ ​ ​ ​\t"
    embed=discord.Embed(title="**Où nous retrouver ?**", color=0x7ec75b)
    embed.set_thumbnail(url="https://cdn.helloasso.com/img/logos/efrei%203d-8fe1b94ab4c44666ac64ffc89ae19641.png")
    embed.add_field(name="Nos locaux", value='Sur le campus République, 1er étage du bâtiment E, à côté des salles de réunion.')
    embed.add_field(name="Nos Réseaux Sociaux", value=f'**[Instagram](https://www.instagram.com/efrei3d/){spacing}[Facebook](https://www.facebook.com/EFREI-3D-1437461196500261/){spacing}[YouTube](https://www.youtube.com/channel/UCrfy0ypHEe8B03LwIgM1WTg)**\n', inline=False)
    embed.add_field(name="Notre Discord", value=f'**[Efrei3D](https://discord.gg/mk4bXtnVYx)**', inline=False)
    embed.add_field(name="Nos Réseaux Professionels", value=f'**[Linkedin](https://www.linkedin.com/company/efrei-3d)**\n', inline=False)
    embed.add_field(name="Nos portfolios", value=f'**[SketchFab](https://www.sketchfab.com/efrei3d){spacing}[Github](https://www.github.com/Efrei3D)**\n', inline=False)
    embed.set_footer(text="Efrei3D: Parce que la réalité ne nous suffit pas 🦖")
    await ctx.send(embed=embed)


@bot.command(name = "give_role",
                        usage = '',
                        description = "give roles to new members")
@commands.has_permissions(manage_nicknames=True, manage_roles=True)
async def give_role(ctx):
    if ctx.guild.id == 537993091228106752: # guild id for Efrei3D
        run_api()
        print('\n')
        with open("short_memberlist.json", 'r') as f: memberlist = json.load(f)
        for element in memberlist:
            member_role = discord.utils.get(user_dscd.guild.roles, name = "Membre 2022-2023")
            user_data, user_dscd = memberlist[element], memberlist[element]["discord"]
            converter = commands.MemberConverter()
            user_dscd = await converter.convert(ctx, user_dscd)
            guild = bot.get_guild(ctx.guild.id)
            if guild.get_member(user_dscd.id):
                if member_role in user_dscd.roles:
                    await user_dscd.add_roles(member_role)
                if user_dscd.nick != f'{user_data["firstname"]} {user_data["lastname"]}':
                    await user_dscd.edit(nick=f'{user_data["firstname"]} {user_data["lastname"]}')
                print(f'\"{user_dscd}\" roles and nicks were updated\n')
            else:
                await ctx.send(f'\"{user_dscd}\" isn\'t on the server and couldn\'t be renamed')
                print(f'\"{user_dscd}\" isn\'t on the server and couldn\'t be renamed')
        await ctx.send("all new users roles and nicks were updated")
        print("all new users roles and nicks were updated")
    else: await ctx.send("Disabled in this server. (sorry 🥺)")


# starting and running the bot
if __name__ == "__main__":
    os.system('cls') if platform.system()=="Windows" else os.system('clear')
    # asyncio.run(main())
    # main()
    bot.run(token)