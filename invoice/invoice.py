import discord


class In_voice:
    """Gives the role 'voice' to anyone who enters a voice channel. THIS ROLE MUST EXIST AND THE BOT MUST HAVE THE RIGHTS TO CHANGE PERMISSIONS FOR IT TO WORK!"""
    def __init__(self, bot):
        self.bot = bot

    async def listener(self, before, after):
        server = after.server
        try:
            for role in server.roles:
                if role.name == 'voice':
                    if role in after.roles:
                        await self.bot.remove_roles(after, role)
                    elif role not in after.roles:
                        await self.bot.add_roles(after, role)
        except discord.errors.Forbidden:
            print('COG DEBUG [INVOICE]: No permissions to change roles.')


def setup(bot):
    n = In_voice(bot)
    bot.add_listener(n.listener, 'on_voice_state_update')
    bot.add_cog(n)