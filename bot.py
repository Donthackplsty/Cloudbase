import hikari
import lightbulb
import miru
import os
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(
    token=os.getenv('TOKEN'), 
    default_enabled_guilds=(890691477892632627),
    intents=hikari.Intents.GUILD_MESSAGES)

miru.load(bot)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass

@my_group.child
@lightbulb.command('subcommand', 'this is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I\'m a subcommand!')

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

bot.load_extensions_from(f'./extensions')

bot.run()