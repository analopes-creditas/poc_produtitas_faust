import os
import app
import models.data_product as model
import workers.create_data_product.controller as controller


principal_topic = app.topic(
    os.getenv('TOPIC_PIPELINE','produtitas-pipeline'),
    value_type=model.DataProductCreate)


@app.agent(principal_topic)
async def consumer(stream):
    async for key, event in stream.items():
        if event.action == 'create_data_product':
            yield controller.DataProductCreate().process(
                key=key.decode('utf-8'), value=event)
