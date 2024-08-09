from pydantic_settings import BaseSettings
from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()


class ArtifactsSettings(BaseModel):
    API_BASE_URL: str
    API_TOKEN: str


class Settings(BaseSettings):
    ARTIFACTS: ArtifactsSettings

    class Config:
        env_file = '.env'
        env_nested_delimiter = "__"


settings = Settings()
