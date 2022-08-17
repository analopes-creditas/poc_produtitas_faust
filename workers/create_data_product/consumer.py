import os
from app import app
from workers.create_data_product.controller import process
from models.data_product import DataProductCreate


principal_topic = app.topic(os.getenv('TOPIC_PIPELINE', 'produtitas-pipeline'), value_type=DataProductCreate)

@app.agent(principal_topic)
async def consumer(events):
    async for event in events:
        if event.action != 'create':
            continue
        yield process(value=event)
