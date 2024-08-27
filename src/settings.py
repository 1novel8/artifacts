from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()
ENV_FILE = '.env'


class Artifacts(BaseSettings):
    api_base_url: str = 'https://api.artifactsmmo.com'
    api_token: str

    model_config = SettingsConfigDict(env_file=ENV_FILE, env_prefix='ARTIFACTS_')


class Settings(BaseSettings):
    artifacts: Artifacts = Artifacts()


settings = Settings()
