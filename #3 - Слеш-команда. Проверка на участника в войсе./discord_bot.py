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

# РЕЗУЛЬТАТ - Вид в дискорде #3.png
@bot.slash_command(name="войс") # создаем слеш команду и даем ей название
async def checkvoice(interaction: disnake.ApplicationCommandInteraction, member: disnake.Member): # создаем функцию с нужными аргументами
    voice = member.voice # получаем голосовой канал пользователя
    if voice is not None: # проверка: если голосовой канал есть
        await interaction.response.send_message(f"{member.mention} **в** голосовом канале: {voice.channel.mention}") # отвечаем автору сообщения (response). используем ** для форматирования текста (жирный)
    else: # если голосового канала нету
        await interaction.response.send_message(f"{member.mention} **не** в голосовом канале") # отвечаем автору сообщения (response). используем ** для форматирования текста (жирный)




bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)
