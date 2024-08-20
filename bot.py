import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'proj.settings'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
import enum
from re import A
import typing
import bot_settings as settings
import discord
from discord.ext import commands
from discord import app_commands
from base.models import *
from bot_files import fee_cmd, room_cmd, task_cmd

logger = settings.logging.getLogger("bot")

class Food(enum.Enum):
    apple = 1
    banana = 2
    cherry = 3

def run():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!",intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        bot.tree.copy_global_to(guild=settings.GUILDS_ID)
        await bot.tree.sync(guild=settings.GUILDS_ID)

    @bot.tree.command(name="get-fee")
    async def get_fee(interaction: discord.Interaction):
        await fee_cmd.get_fee_command(interaction)

    @bot.tree.command(name="set-fee")
    @app_commands.describe(fee="Please Provide the fee like 5%")
    @app_commands.rename(fee="fee")
    @commands.is_owner()
    async def set_fee(interaction: discord.Interaction, fee : str):
        await fee_cmd.set_fee_command(interaction, fee)


    @bot.tree.command(name="create-room")
    @commands.is_owner()
    async def create_room(interaction: discord.Interaction, artist: discord.Member, influencer: discord.Member):
        await room_cmd.create_room_command(interaction, artist, influencer)

    @bot.tree.command(name="tasks")
    @commands.is_owner()
    async def tasks(interaction: discord.Interaction):
        await task_cmd.get_all_tasks(interaction)

    @bot.tree.command(name="add-task")
    @app_commands.describe(task="Add a task")
    @app_commands.rename(task="task")
    @commands.is_owner()
    async def add_task(interaction: discord.Interaction, task : str):
        await task_cmd.create_task(interaction, task)

    @bot.tree.command(name="remove-task")
    @app_commands.describe(task="Delete a task")
    @app_commands.rename(task="task")
    @commands.is_owner()
    async def remove_task(interaction: discord.Interaction, task : str):
        await task_cmd.delete_task(interaction, task)

    # @bot.tree.command()
    # @app_commands.describe(text_to_send="Simon says this..")
    # @app_commands.rename(text_to_send="message")
    # async def say(interaction: discord.Interaction, text_to_send : str):
    #     await interaction.response.send_message(f"{text_to_send}", ephemeral=True)

    # @bot.tree.command()
    # async def drink(interaction: discord.Interaction, choice: typing.Literal['beer', 'milk', 'tea']):
    #     await interaction.response.send_message(f"{choice}", ephemeral=True)

    # @bot.tree.command()
    # async def eat(interaction: discord.Interaction, choice: Food):
    #     await interaction.response.send_message(f"{choice}", ephemeral=True)

    # @bot.tree.command()
    # @app_commands.choices(choice=[
    #     app_commands.Choice(name="red", value="1"),
    #     app_commands.Choice(name="blue", value="2"),
    #     app_commands.Choice(name="green", value="3"),
    # ])
    # async def color(interaction: discord.Interaction, choice: app_commands.Choice[str]):
    #     await interaction.response.send_message(f"{choice.name} : {choice.value}", ephemeral=True)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
