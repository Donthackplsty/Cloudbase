import hikari
import lightbulb
import platform

plugin = lightbulb.Plugin('admin')

@plugin.command
@lightbulb.command('admin', "admin commands")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def admin_group(ctx):
   pass

@admin_group.child
@lightbulb.command('system', 'prints info about the system')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def system(ctx):
    embed=hikari.Embed(title="" , color=0x06eae6)
    embed.set_author(name="System Information")
    embed.add_field(name="Machine", value=platform.machine(), inline=False)
    embed.add_field(name="Platform", value=platform.platform(), inline=False)
    embed.add_field(name="System", value=platform.system(), inline=False)
    embed.add_field(name="Processor", value=platform.processor(), inline=False)
    await ctx.respond(embed=embed)

def load(bot):
    bot.add_plugin(plugin)