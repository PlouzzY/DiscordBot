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


@bot.slash_command(name="эмбеды")    
async def embeds(interaction: disnake.ApplicationCommandInteraction,
                 text1,
                 text2,
                 text3):
    embed0 = disnake.Embed()
    embed0.set_image(url="https://cdn.discordapp.com/attachments/1226137751531950171/1236700111388545105/image.png?ex=663c41fb&is=663af07b&hm=7325bdf3abb1bbff50c28ee40f2e4f65249fb1c11e44f6b4cdbc4a8517f70a09&")
    embed1 = disnake.Embed(title="Первый эмбед", description=f"{text1}", color=disnake.Colour.green())
    embed2 = disnake.Embed(title="Второй эмбед", description=f"{text2}", color=disnake.Colour.yellow())
    embed3 = disnake.Embed(title="Третий эмбед", description=f"{text3}", color=disnake.Colour.red())
    embeds = [embed0, embed1, embed2, embed3]
    await interaction.response.send_message(embeds=embeds)



    

bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)




