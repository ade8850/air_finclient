from dependency_injector import containers, providers
from .config import Settings
from airtable import client


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.from_dict(Settings().model_dump())

    client = providers.Singleton(
        client.AirtableFinClient,
        config.airtable_api_key,
        config.airtable_base_id,
        config.airtable_tbl_months_id,
        )
    
    