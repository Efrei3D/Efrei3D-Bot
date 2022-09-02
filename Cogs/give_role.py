import discord
from discord.ext import commands
import json

class give_roleCog(commands.Cog, name="give_role command"):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    
    @commands.command(name = "give_role",
                        usage = '',
                        description = "give roles to new members")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def give_role(self, ctx):
        with open("short_memberlist.json", 'r') as f: memberlist = json.load(f)
        for element in memberlist:
            user_data, user_dscd = memberlist[element], memberlist[element]["discord"]
            converter = commands.MemberConverter()
            user_dscd = await converter.convert(ctx, user_dscd)
            await user_dscd.add_roles(discord.utils.get(user_dscd.guild.roles, name = "Membre 2022-2023"))
            print(f'role given to {user_data["firstname"]} {user_data["lastname"]}')
            await user_dscd.edit(nick=f'{user_data["firstname"]} {user_data["lastname"]}')
            print(f'{user_dscd} nick was changed to \"{user_data["firstname"]} {user_data["lastname"]}\"\n\n')
            await ctx.channel.send("all new users roles and nicks were updated")


async def setup(bot):
    await bot.add_cog(give_roleCog(bot))