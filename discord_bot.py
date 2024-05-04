import disnake
from disnake.ext import commands


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("бот запущен")
    await bot.change_presence(activity=disnake.Game(name="игры")) # активность бота, статус бота

@bot.command(name="пинг")
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention}, понг!")


bot.run("MTE3MDM2NTEwODM1OTI3ODYzMw.GEPdNq.M1pzel2jlcX7CCfoIDA459QCbtLRm5VaUKj1M0")
