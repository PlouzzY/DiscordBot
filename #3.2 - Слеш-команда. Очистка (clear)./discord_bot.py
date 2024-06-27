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


@bot.slash_command(name="очистить", description="удалить определенное количество сообщений") # создаем слеш-команду. Даем ей название и устанавливаем описание
async def clear(interaction: disnake.ApplicationCommandInteraction, limit: int = 0): # создаем функцию. limit: int = 0 - Позваляет нам сделать аргумент limit необязательным, где стандартное значение 0
    if limit > 100: # если лимит больше 100
        return await interaction.response.send_message("Максимальный лимит - 100 сообщений!", ephemeral=True) # возвращаем ошибку с недопустимым лимитом
    await interaction.response.defer() # бот в ожидании (избавляемся от ошибки интеграции)
    count_deleted = await interaction.channel.purge(limit=limit+1) # удаляем сообщения по лимиту (+1 для того, чтобы удалялось использование команды)
    await interaction.channel.send(f"Было удалено - {len(count_deleted)-1} сообщений") # отправляем сообщение в канал, в котором использовалась команда (-1 для того, чтобы бот не считал использование команды как удаленное сообщение)



bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)