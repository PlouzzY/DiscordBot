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
@bot.command(name="эмбед") # создаем команду и даем ей название
async def embed(ctx): # в функцию передаем аргумент context
    Name = disnake.Embed(title="Заголовок", description="Описание эмбеда", color=disnake.Colour.green()) # создаем эмбед (для удобства заменяйте Name на embed)
    Name.add_field(name='Заголовок1', value=f'Текст1', inline=False) # добавляем в эмбед строки
    Name.add_field(name='Заголовок2', value=f'Текст2', inline=False) # добавляем в эмбед строки
    Name.set_thumbnail(url="https://cdn.discordapp.com/attachments/1226137751531950171/1236699842848362607/image.png?ex=6638f5fb&is=6637a47b&hm=74d23b6da36c06cbe798b78587002b2efae6cc4340e4ff41b852247f656b4ac7&") # устанавливаем картику (справа сверху)
    Name.set_image(url="https://cdn.discordapp.com/attachments/1226137751531950171/1236700111388545105/image.png?ex=6638f63b&is=6637a4bb&hm=0f93c180559e20c2dc5d839aca82b14cbd2a95ff8ac6f8bf82539beadfd60fe0&") # устанавливаем баннер (снизу)
    await ctx.send(embed=Name) # отправляем эмбед





bot.run("токен")  # запуск бота (токен можно получить на портале разработчика)
