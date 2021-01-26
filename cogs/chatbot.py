import discord
from discord.ext import commands
import async_cleverbot as ac


class CleverbotCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.cleverbot = ac.Cleverbot("[9&ph)c7my1[yRbzqcyD")
        self.cleverbot.set_context(ac.DictContext(self.cleverbot))

    @commands.command(name="RKS")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def RKS_(self, ctx, *, query: str):
        await ctx.trigger_typing()
        try:
            r = await self.cleverbot.ask(query, ctx.author.id)
        except ac.InvalidKey:
            return await ctx.send(
                "An error has occurred. The API key provided was not valid."
            )
        except ac.APIDown:
            return await ctx.send("I have to sleep sometimes. Please ask me later!")
        else:
            await ctx.send("{}, {}".format(ctx.author.mention, r.text))

    def cog_unload(self):
        self.bot.loop.create_task(self.cleverbot.close())


def setup(bot):
    bot.add_cog(CleverbotCog(bot))
