import discord
from discord.ext import commands

class stop_cmdCog(commands.Cog, name="stop command"):
    def __init__(self, bot:commands.bot):
        self.bot = bot

    
    @commands.command(name = "stop",
                        usage = '',
                        description = "shutsdown the bot",
                        aliases = ['sd'])
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def stop_cmd(self, ctx):
        await ctx.send("https://tenor.com/view/star-wars-darth-vader-noo-no-gif-15893771")
        exit()


async def setup(bot):
    await bot.add_cog(stop_cmdCog(bot))