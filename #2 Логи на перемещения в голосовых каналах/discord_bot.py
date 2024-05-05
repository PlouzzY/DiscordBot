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


@bot.event # создаем ивент. для сокращения места, голосовой канал я буду заменять на войс
async def on_voice_state_update(member, before, after): # функция работает при изменении в войсах. передаем аргументы пользователя, предыдущего войса (откуда вышли), настоящего войса (куда зашли)
    LogChnl = bot.get_channel(1225114215170310207) # определяем текстовой канал, куда будут скидываться сообщения при срабатывании ивента
    
    if before.channel is None and after.channel is not None: # проверка: если прошлого войса нет и настоящий войс есть (зашел)
        await LogChnl.send(f"{member.mention} зашел в голосовой канал {after.channel.mention}") # отправляем сообщение в ранее указаный текстовой канал (after.channel.mention - упоминание настоящего войса)
    
    elif before.channel is not None and after.channel is None: # проверка: если прошлый войс есть и настоящего войса нет (вышел)
        await LogChnl.send(f"{member.mention} покинул голосовой канал {before.channel.mention}") # так же отправляем сообщение (before.channel.mention - упоминание предыдущего канала)
    
    elif before.channel is not None and after.channel is not None: # проверка: если прошлый канал есть и настоящий канал есть (переместился)
        await LogChnl.send(f"{member.mention} переместился из голосового канала {before.channel.mention} в канал {after.channel.mention}") # так же отправляем сообщение


    # Таким образом можно делать логи на голосовые каналы
    
    # Можно добавить проверку, если after.channel является каким-то каналом, то пользователю будет выдаваться роль, если after.channel не является этим каналом, то роль снимается
    
    # Так же, можно создавать авто войсы (пользователь зашел в определенный канал -> бот создал новый войс и переместил туда зашедшего -> если пользователь покидает созданный канал, то он удаляется)
    
    # Можно сделать что-то типо приват войса, т.е при заходе в определенный канал, у пользователя автоматически выключается микрофон
    # Для этого мы получаем приватный канал (privateChnl = bot.get_channel(id))
    # И дальше пишем, если after.channel is privateChnl -> await member.edit(mute = True) (можно сравнивать через id канала: after.channel.id == id)
    # Если after.channel is not privateChnl -> await member.edit(mute = False)



bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)




