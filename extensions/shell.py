import hikari
import lightbulb
import miru
import subprocess

plugin = lightbulb.Plugin('shell')

class Confirm(miru.View):

    @miru.button(label="Confirm", style=hikari.ButtonStyle.SUCCESS)
    async def confirm_button(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond("Okay, I'll run the command!")
        self.stop()

    @miru.button(label="Cancel", style=hikari.ButtonStyle.DANGER, row=2)
    async def cancel_button(self, button: miru.Button, ctx: miru.Context) -> None:
        await ctx.respond('Okay, I cancelled your command')
        self.stop() # Stop listening for interactions


@plugin.listener(hikari.GuildMessageCreateEvent)
async def buttons(event: hikari.GuildMessageCreateEvent) -> None:

    # Do not process messages from bots or empty messages
    if event.is_bot or not event.content:
        return

    if event.content.startswith("shell.run"):
        view = Confirm()

        if event.content == "shell.run":
            await event.message.respond("You have not written any command!")
            return
        
        else:
            command = event.content[10:]
            message = await event.message.respond(f"You are about to run this command `{command}`", components=view.build())
            view.start(message)  # Start listening for interactions
            await view.wait()  # Wait until the view is stopped or times out

def load(bot):
    bot.add_plugin(plugin)