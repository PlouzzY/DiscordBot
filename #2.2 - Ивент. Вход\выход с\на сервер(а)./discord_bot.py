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
async def on_member_join(member): # функция срабатывает, если пользователь присоединился к серверу
    chnlJoin = bot.get_channel(1225114215170310207) # получаем канал, в который будут скидываться сообщения о заходе
    await chnlJoin.send(f"✅ {member.mention} зашел на сервер! \n Это уже {member.guild.member_count} участник.") # отправляем сообщение (можно сделать через эмбед)

@bot.event # создаем ивент
async def on_member_remove(member): # функция срабатывает, если пользователь покинул сервер
    chnlExit = bot.get_channel(1225114215170310207) # получаем канал, в который будут скидываться сообщения о выходе
    await chnlExit.send(f"❌ {member.mention} покинул сервер! \n Это уже {member.guild.member_count} участник.") # отправляем сообщение (можно сделать через эмбед)





bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)
