# импортируем библиотеки (я работаю с disnake, есть еще discord.py)
import disnake
from disnake.ext import commands
from datetime import datetime # для работы со временем

intents = disnake.Intents.all() # определяем разрешения
bot = commands.Bot(command_prefix="=", intents=intents) # устанавливаем префикс и разрешения
bot.remove_command("help") # удаляем встроенную команду help 


@bot.event # создаем ивент
async def on_ready(): # функция срабатывает, если бот запустился
    print("бот запущен") # получаем сообщение при запуске бота
    await bot.change_presence(activity=disnake.Game(name="игры"), status=disnake.Status.online) # ставим активность и статус бота


# РЕЗУЛЬТАТ - Вид в дискорде
@bot.event # создаем ивент
async def on_message_edit(before: disnake.Message, after: disnake.Message): # функция срабатывает, если сообщение было отредактировано (before - прошлое сообщение, after - новое сообщение)
    chnllog = bot.get_channel(1225114215170310207) # получаем канал, в который будут скидываться сообщения о редактировании
    time = (disnake.utils.format_dt(datetime.now(), style='D')) # получаем время (style='D' позволяет в будущем наводиться на время, для получения точной даты) 
    embed = disnake.Embed(title=f"Редактирование сообщения", description=f"Пользователь: {after.author.mention} \nКанал: {after.channel.mention} \nВремя: {time}", color=disnake.Colour.yellow()) # создание эмбеда
    embed.add_field(name="Прошлое содержание: ", value=f"> {before.content}", inline=False) # добовляем строки (.content - позволяет увидеть содержимое этого сообщения)
    embed.add_field(name="Новое содержание: ", value=f"> {after.content}", inline=False) # добовляем строки (.content - позволяет увидеть содержимое этого сообщения)
    embed.set_thumbnail(url=after.author.display_avatar) # устанавливаем аватарку пользователя, который отредактировал сообщение
    await chnllog.send(embed=embed) # отправляем сообщение





bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)




