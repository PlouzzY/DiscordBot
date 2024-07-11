# импортируем библиотеки (я работаю с disnake, есть еще discord.py)
import disnake
from disnake.ext import commands
import os

intents = disnake.Intents.all() # определяем разрешения
bot = commands.Bot(command_prefix="=", intents=intents) # устанавливаем префикс и разрешения
bot.remove_command("help") # удаляем встроенную команду help 


for file in os.listdir("./cogs"): # перебираем папку cogs
    if file.endswith(".py"): # проверка: если файл с расширением "py"
        bot.load_extension(f"cogs.{file[:-3]}") # подгружаем этот файл


@bot.event # создаем ивент
async def on_ready(): # функция срабатывает, если бот запустился
    print("бот запущен") # получаем сообщение при запуске бота
    await bot.change_presence(activity=disnake.Game(name="игры"), status=disnake.Status.online) # ставим активность и статус бота





bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)