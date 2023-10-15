import discord


class BaseClient(discord.Client):
    async def on_ready(self):
        print('bot is ready')


class VoiceClient(discord.VoiceClient):
    async def on_message(self, message: discord.Message):
        channel = message.author.voice.channel
        print(self.client.status)
        await channel.connect()


