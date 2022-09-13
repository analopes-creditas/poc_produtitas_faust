import os
from core.workers.app import create_app
import core.utils.constants as const
import core.models.data_product as model
import core.workers.data_product.controller as controller


app = create_app(app_name='data_product')
principal_topic = app.topic(os.getenv('TOPIC_PIPELINE'), value_type=model.DataProduct)


@app.agent(principal_topic)
async def consumer(stream):
    async for event in stream:
        if event.action == const.ACTION_CREATE:
            yield controller.DataProduct().create(value=event)
