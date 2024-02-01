from pydantic import BaseSettings, PostgresDsn


class _Config(BaseSettings):
    DATABASE_URL: PostgresDsn


config = _Config()
