import discord
from discord.ext import commands

from yandex.base import ya_client, YaClient


class BaseBot(discord.Client):
    async def on_ready(self):
        print('bot is ready')


intents = discord.Intents().all()
client = BaseBot(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='join')
async def join_bot_to_voice(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command(name='leave')
async def leave_bot_from_voice(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='play')
async def play_song(
    ctx,
    url,
    yandex_client: YaClient = ya_client
):
    voice_client = ctx.message.guild.voice_client
    track_url = await yandex_client.get_sound_url(url)
    if not voice_client:
        await join_bot_to_voice(ctx)
        await play_song(ctx, url)
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice_client.play(discord.FFmpegOpusAudio(source=track_url))
