import os
import core.app as app
import core.utils.constants as const
import core.models.data_product as model
import core.workers.create_data_product.controller as controller


principal_topic = app.topic(os.getenv('TOPIC_PIPELINE', ''), value_type=model.DataProduct)


@app.agent(principal_topic)
async def consumer(stream):
    async for event in stream:
        if event.action == const.ACTION_CREATE:
            yield controller.DataProduct().create(value=event)
