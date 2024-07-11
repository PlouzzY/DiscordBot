import disnake
from disnake.ext import commands 



class StartCogCog1(commands.Cog): # создаем класс и даем ему название

    def __init__(self, bot: commands.Bot): # добавляем инициализацию в класс
        self.bot = bot # создаем переменную для будущей работы с ней

    @commands.Cog.listener() # создаем ивент (замена синтаксиса в файле - Описание #7)
    async def on_ready(self): # в функцию передаем аргумент self, так как это обязательный аргумент в когах
        print("Ког Cog1 запущен") # получаем сообщение при запуске кога


class CommandCog1Class(commands.Cog): # создаем класс и даем ему название

    def __init__(self, bot: commands.Bot): # добавляем инициализацию в класс
        self.bot = bot # создаем переменную для будущей работы с ней

    # РЕЗУЛЬТАТ - Вид в дискорде
    @commands.command(name="ког1") # создаем команду и даем ей название (замена синтаксиса в файле - Описание #7)
    async def cogCMD1(self, ctx): # в функцию передаем аргумент self, так как это обязательный аргумент в когах
        await ctx.send("Ког1!") # отправляем сообщение
        






def setup(bot): # создаем функцию, которая принимает аргумент "bot"
    bot.add_cog(StartCogCog1(bot)) # добавляем класс
    bot.add_cog(CommandCog1Class(bot)) # добавляем класс
