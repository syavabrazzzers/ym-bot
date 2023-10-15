from bot.base import bot

from settings import settings

if __name__ == "__main__":
    bot.run(settings.DISCORD_TOKEN)
