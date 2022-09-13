import os
import core.app as app


source_topic = app.topic(os.getenv('TOPIC_RAW_METADATA', ''))
destiny_topic = app.topic(os.getenv('TOPIC_PIPELINE', ''))


def format(data: dict) -> dict:
    return {
        'record': data.after.json,
        'action': data.op
    }


@app.agent(source_topic)
async def consumer(stream):
    async for event in stream:
        print(f"event: {event}")
        change = format(event.payload)
        print(f"change: {change}")
        change.forward(destiny_topic)
