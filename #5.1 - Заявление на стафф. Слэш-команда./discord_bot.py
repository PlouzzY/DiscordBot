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
# Так же читайте описание команды - Описание #5
@bot.slash_command(name="заявка1") # создаем слэш-команду и даем ей название
async def statement1(interaction: disnake.ApplicationCommandInteraction, # передаем аргументы (можно в все в одну строчку)
                     name = commands.Param(name="имя", description="Ваше полное имя"),
                     age = commands.Param(name="возраст", description="Ваш полный возраст"),
                     online = commands.Param(name="актив", description="Ваш средний онлайн в день")):
    try: # пробуем парсировать age в int
        if int(age) < 15: # если возраст меньше 15
            return await interaction.response.send_message("Набор на должность строго с 15 лет!") # возвращаем ошибку
    except: # если age нельзя парсировать в int
        return await interaction.response.send_message("Введите возраст правильно!") # возвращаем ошибку
    
    await interaction.response.send_message("Заявление отправлено!") # Уведомляем, что все прошло успешно
    StatementChnl = bot.get_channel(1225114215170310207) # указываем канал в который будет отправляться заявление (канал сделать закрытым - для конфиденциальности)
    embed = disnake.Embed(title="Заявление", description=f"Автор: {interaction.author.mention}", color=disnake.Colour.yellow())  # создаем эмбед и настраиваем под себя (Эмбед разбирал в #4 директории)
    embed.add_field(name="Имя", value=f"> {name}", inline=False)
    embed.add_field(name="Возраст", value=f"> {age}", inline=False)
    embed.add_field(name="Онлайн", value=f"> {online} ч./день", inline=False)
    embed.set_thumbnail(url=interaction.author.display_avatar) # устанавливаем отображаемый аватар отправителя команды
    await StatementChnl.send(embed=embed) # отправляем заявление в админ-канал.


bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)




