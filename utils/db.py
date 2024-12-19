from sqlalchemy import create_engine, text as parsed_query, Connection, Engine

def get_snowflake_engine() -> Engine:
    engine = create_engine(
        'snowflake://{user}:{password}@{account_identifier}/{database}/{schema}?warehouse={warehouse}&role={role}'.format(
            user='static_scrapper_user',
            password='static_scrapper_password',
            account_identifier='RG94457.EU-CENTRAL-1',
            database='static_scrapper',
            schema='public',
            warehouse='static_scrapper_warehouse',
            role='static_scrapper_role',
        ), echo=True
    )
    
    return engine
