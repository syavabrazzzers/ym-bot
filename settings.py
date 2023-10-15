from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path.cwd() / '.env'


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE
    )

    DISCORD_TOKEN: str
    YM_KEY: str


settings: AppSettings = AppSettings()
