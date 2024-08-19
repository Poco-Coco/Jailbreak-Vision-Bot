import nextcord
import os
import time
import asyncio
import cooldowns

from nextcord.ext import commands

# Configs
TOKEN = "YOUR_BOT_TOKEN"
OWNER_ID = 00000000000
intents = nextcord.Intents.all()
emcolor = 0x8042A9

bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)
bot.remove_command("help")


async def setup():
    cogs = 0
    for filename in os.listdir("./raphsmanager/cogs"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"Cogs: {filename[:-3]} is ready!")

                cogs += 1
            except Exception as e:
                print(f"Unable to load {filename[:-3]} Error: {e}")
        else:
            print(f"Passed file/folder {filename[:-3]}")

    return cogs


async def reloadSetup():
    cogs = 0
    for filename in os.listdir("./raphsmanager/cogs"):
        if filename.endswith(".py"):
            try:
                bot.reload_extension(f"cogs.{filename[:-3]}")
                print(f"Cogs: {filename[:-3]} is reloaded!")
                cogs += 1
            except Exception as e:
                print(f"Unable to reload {filename[:-3]} Error: {e}")
        else:
            print(f"Passed file/folder {filename[:-3]}")

    return cogs


@bot.event
async def on_ready():
    await bot.delete_unknown_application_commands()
    print("Main Bot is Online")


@bot.event
async def on_application_command_error(interaction: nextcord.Interaction, error):
    error = getattr(error, "original", error)

    if isinstance(error, cooldowns.CallableOnCooldown):
        convert = time.strftime("%H:%M:%S", time.gmtime(error.retry_after))

        await interaction.send(
            f"You are currently on a cooldown! Retry in `{convert}`!"
        )

    else:
        raise error


@bot.command()
async def reloadcogs(ctx):
    await bot.delete_unknown_application_commands()
    if ctx.author.id == OWNER_ID:
        newcogs = await setup()
        reloadedcogs = await reloadSetup()
        await ctx.send(f"Reloaded {reloadedcogs} cogs, loaded {newcogs} new cogs.")
    else:
        await ctx.send("You don't have permission haha!")


@bot.slash_command(
    name="list",
    description="Shows all the servers I am in!",
)
async def list(
    interaction: nextcord.Interaction,
):
    Para = ""
    for guild in bot.guilds:
        Para = Para + f"Guild: {guild.name} | Member: {guild.member_count}\n"

    await interaction.response.send_message(Para)


asyncio.run(setup())
bot.run(TOKEN)
