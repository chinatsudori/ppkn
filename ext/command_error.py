import discord
from discord.ext import commands
import random
from lib.error_handler import log_error


class CommandErrorEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # Use logging instead of print for better error management
        log_error(f"An error occurred with the command '{ctx.command}': {error}")

        # Simplify error message construction
        error_message = (
            f"**Error:** An error occurred with the command '{ctx.command}': {error}"
        )
        await ctx.send(error_message)

        if isinstance(error, commands.CommandNotFound):
            responses = [
                "Dururururu~",
                "Nyaanya~",
                "Pyon pyon pyoon~",
                "Kira kira~",
                "Mofu mofu~",
                "Uauuuuuu~",
                "Wan wan~",
                "kyuuuuuun~",
                "*Angrykotsounds*",
            ]
            chosen_response = random.choice(responses)
            error_embed = discord.Embed(
                title="bzzzzt~", description=chosen_response, color=discord.Color.red()
            )
            await ctx.send(embed=error_embed)
        else:
            # Handle other errors not specifically caught by the above
            log_error(f"Unhandled error: {error}")


async def setup(bot):
    await bot.add_cog(CommandErrorEvents(bot))
