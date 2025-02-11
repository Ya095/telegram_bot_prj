from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ищем нужные значения в переменных окружения
    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    bot_token: str
    admin_ids: frozenset[int] = frozenset({42, 693795034})


settings = Settings()
