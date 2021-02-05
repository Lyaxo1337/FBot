from discord.ext import commands
from discord import Embed

class links(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="invite")
    async def _Invite(self, ctx):
        fn = self.bot.fn
        await ctx.send(embed=fn.embed("Invite FBot to your server!", url=fn.invite))

    @commands.command(name="server")
    async def _Server(self, ctx):
        fn = self.bot.fn
        await ctx.send(embed=fn.embed("Join our server, it's for support and fun!", url=fn.server))

    @commands.command(name="links")
    async def _Links(self, ctx):
        fn = self.bot.fn
        embed = fn.embed("FBot links")
        embed.add_field(name="Support server", value=f"[click here]({fn.server})")
        embed.add_field(name="Invite FBot", value=f"[click here]({fn.invite})")
        embed.add_field(name="Our website", value=f"[click here]({fn.site})")
        embed.add_field(name="Top.gg page", value=f"[click here]({fn.top})")
        embed.add_field(name="Top.gg vote", value=f"[click here]({fn.votetop})")
        embed.add_field(name="FBot's github", value=f"[click here]({fn.github})")
        embed.add_field(name="discordbotlist page", value=f"[click here]({fn.dbl})")
        embed.add_field(name="discordbotlist vote", value=f"[click here]({fn.votedbl})")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(links(bot))
