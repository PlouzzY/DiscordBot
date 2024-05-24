# импортируем библиотеки (я работаю с disnake, есть еще discord.py)
import disnake
from disnake.ext import commands
import datetime # для работы со временем

intents = disnake.Intents.all() # определяем разрешения
bot = commands.Bot(command_prefix="=", intents=intents) # устанавливаем префикс и разрешения
bot.remove_command("help") # удаляем встроенную команду help 


@bot.event # создаем ивент
async def on_ready(): # функция срабатывает, если бот запустился
    print("бот запущен") # получаем сообщение при запуске бота
    await bot.change_presence(activity=disnake.Game(name="игры"), status=disnake.Status.online) # ставим активность и статус бота

# РЕЗУЛЬТАТ - Вид в дискорде
# Импортируйте библиотеку!
@bot.event # создаем ивент
async def on_message_delete(message: disnake.Message): # функция срабатывает, если сообщение было удалено
    chnllog = bot.get_channel(1225114215170310207) # получаем канал, в который будут скидываться сообщения о удалении
    ctx = await bot.get_context(message) # заносим сообщение в переменную
    if message.author.bot or ctx.command: # проверяем, что автор сообщения бот ИЛИ сообщение является командой
        return # возвращаем (остонавливаем функцию)
    async for deleted_by in message.guild.audit_logs(action=disnake.AuditLogAction.message_delete, limit=1): # получаем пользователя (который удалил сообщение) через аудит сервера
        time = (disnake.utils.format_dt(datetime.datetime.now(), style='D')) # получаем время (style='D' позволяет в будущем наводиться на время, для получения точной даты) 
        embed = disnake.Embed(title=f"Удаление сообщения", description=f"Автор сообщения: {message.author.mention} \nУдалил сообщение: {deleted_by.user.mention} \nКанал: {message.channel.mention} \nВремя: {time}", color=disnake.Colour.red()) # создание эмбеда
        embed.add_field(name="Содержание: ", value=f"> {message.content}", inline=False) # добавляем строки (.content - позволяет увидеть содержимое этого сообщения)
        embed.set_thumbnail(url=message.author.display_avatar) # устанавливаем аватарку пользователя, чье сообщение было удалено
        await chnllog.send(embed=embed) # отправляем сообщение



bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)
