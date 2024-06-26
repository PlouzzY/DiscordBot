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


@bot.event # создаем ивент
async def on_member_join(member): # функция срабатывает, если пользователь зашел на сервер
    chnlJoin = bot.get_channel(1238525013729214625) # канал в который будут скидываться сообщения о заходе
    await chnlJoin.send(f"✅ {member.mention} зашел на сервер! \n Это уже {member.guild.member_count} участник.") # отправляем сообщение (member.guild.member_count - количество участников на сервере)

@bot.event # создаем ивент
async def on_member_remove(member): # функция срабатывает, если пользователь покинул сервер
    chnlExit = bot.get_channel(1238525013729214625) # канал в который будут скидываться сообщения о выходе
    await chnlExit.send(f"❌ {member.mention} покинул сервер! \n Это был {member.guild.member_count + 1} участник.") # отправляем сообщение (member.guild.member_count - количество участников на сервере)



bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)
