# импортируем библиотеки (я работаю с disnake, есть еще discord.py)
import disnake
from disnake.ext import commands


intents = disnake.Intents.all() # определяем разрешения
bot = commands.Bot(command_prefix="=", intents=intents) # устанавливаем префикс и разрешения
bot.remove_command("help") # удаляем встроенную команду help 


@bot.event # создаем ивент
async def on_ready(): # функция срабатывает когда бот запускается
    print("бот запущен") # получаем сообщение при запуске бота
    await bot.change_presence(activity=disnake.Game(name="игры"), status=disnake.Status.online) # ставим активность и статус бота

@bot.command(name="пинг") # создаем команду и даем название (можно оставить скобки пустыми, тогда для вызова команды упоминаем функцию, т.е - "=ping")
async def ping(ctx): # функция команды, в скобках указываем аргументы, например - (ctx, member: disnake.Member, number: int), функция сразу понимает какой тип у аргумента должен быть
    await ctx.send(f"{ctx.author.mention}, понг!") # отправляем сообщение (ctx.author - автор сообщения, .mention - упоминание)


bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)
