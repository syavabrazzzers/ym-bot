import discord


class BaseClient(discord.Client):
    async def on_ready(self):
        print('bot is ready')


class VoiceClient(discord.VoiceClient):
    async def on_message(self, message: discord.Message):
        channel = message.author.voice.channel
        print(self.client.status)
        await channel.connect()


def main():
    intents = discord.Intents.default()
    intents.message_content = True

    client = VoiceClient(intents=intents)
    client.run('MTE2Mjg2NDU1MDg1NzY4NzEyMA.Gr866k.LHM5zQrUANWx92g-mUIAHRIK1LMYKIo4lSdA8E')
