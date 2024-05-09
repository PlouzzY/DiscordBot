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
@bot.event # создаем ивент
async def on_message(message): # функция срабатывает, если кто-то отправляет сообщение
    await bot.process_commands(message) # игнорирует команды
    if message.author.bot: # проверка: если автор сообщения является ботом
        return
    if message.content == "пинг!": # проверка: если контент сообщения является ""
        await message.channel.send("понг!") # отправляем сообщение в канал, где было получено сообщения пользователя



bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)
