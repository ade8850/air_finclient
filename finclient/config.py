from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    airtable_api_key: str
    airtable_base_id: str
    airtable_tbl_months_id: str

    model_config = SettingsConfigDict(env_prefix='finclient_')