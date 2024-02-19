from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    LOGIN: str
    PASSWORD: str
    CLIENT_ID: int
    CLIENT_SECRET: str


CONFIG = Config()  # type: ignore
