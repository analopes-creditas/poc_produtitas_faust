import os
import app


source_topic = app.topic(
    os.getenv('TOPIC_RAW_METADATA', 'datahub-raw-metadata'))

destiny_topic = app.topic(
    os.getenv('TOPIC_PIPELINE','produtitas-pipeline'))


@app.agent(source_topic)
async def consumer(stream):
    async for event in stream:
        event.forward(destiny_topic)
