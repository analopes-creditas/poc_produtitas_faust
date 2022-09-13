import os
from core.workers.app import create_app


app = create_app(app_name='domain_filter')
source_topic = app.topic(os.getenv('TOPIC_RAW_METADATA', 'dbserver.public.data_product_entity'))
destiny_topic = app.topic(os.getenv('TOPIC_PIPELINE', 'produtitas-pipeline'))


def format(data: dict) -> dict:
    return {
        'record': data.after.json,
        'action': data.op
    }


@app.agent(source_topic)
async def consumer(stream):
    async for event in stream:
        print(f"event: {event}")
    #    change = format(event.payload)
        # print(f"change: {change}")
        event.forward(destiny_topic)
