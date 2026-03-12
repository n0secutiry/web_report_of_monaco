from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):

    PGUSER: str
    PGPASSWORD: str
    PGHOST: str
    PGPORT: int
    PGDATABASE: str

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"


setting = Setting()