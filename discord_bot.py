import disnake
from disnake.ext import commands


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("бот запущен")
    await bot.change_presence(activity=disnake.Game(name="игры"), status=disnake.Status.online) # активность бота, статус бота

@bot.command(name="пинг")
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention}, понг!")


bot.run("токен")
