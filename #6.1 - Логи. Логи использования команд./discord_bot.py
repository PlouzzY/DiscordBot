# импортируем библиотеки (я работаю с disnake, есть еще discord.py)
import disnake
from disnake.ext import commands

intents = disnake.Intents.all() # определяем разрешения
bot = commands.Bot(command_prefix="=", intents=intents) # устанавливаем префикс и разрешения
bot.remove_command("help") # удаляем встроенную команду help 


@bot.event # создаем ивент
async def on_ready(): # функция срабатывает, если бот запустился
    print("бот запущен") # получаем сообщение при запуске бота
    await bot.change_presence(activity=disnake.Game(name="игры"), status=disnake.Status.online) # ставим активность и статус бота

# РЕЗУЛЬТАТ - Вид в дискорде
@bot.command(name="cmd1") # создаем команду и даем название
async def cmd1(ctx, argument1, argument2): # настраиваем команду под себя
    chnllog = bot.get_channel(1225114215170310207) # канал для логов
    embed = disnake.Embed(title="Использование команды", description=f"{ctx.author.mention} \n\n> cmd1 {argument1} {argument2}") # сообщение которое будет скидываться в логи
    await chnllog.send(embed=embed) # отправление сообщения
    await ctx.send("!") # основной код для команды

@bot.command(name="cmd2")
async def cmd1(ctx, argument1, argument2):
    chnllog = bot.get_channel(1225114215170310207)
    embed = disnake.Embed(title="Использование команды", description=f"{ctx.author.mention} \n\n> cmd2 {argument1} {argument2}")
    await chnllog.send(embed=embed)
    await ctx.send("!")

@bot.command(name="cmd3")
async def cmd1(ctx, argument1, argument2):
    chnllog = bot.get_channel(1225114215170310207)
    embed = disnake.Embed(title="Использование команды", description=f"{ctx.author.mention} \n\n> cmd3 {argument1} {argument2}")
    await chnllog.send(embed=embed)
    await ctx.send("!")



bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)




