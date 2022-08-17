import os
from app import app


principal_topic = app.topic(os.getenv('TOPIC_RAW_METADATA', 'datahub-raw-metadata'))

@app.agent(principal_topic)
async def consumer(events):
    async for key, value in events.items():
        if key.decode('utf-8') == 'create_data_product':
            ...
        elif key.decode('utf-8') == 'update_data_product':
            ...
