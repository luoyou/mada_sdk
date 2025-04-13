import asyncio
import json
from redis import asyncio as aioredis

from src.process import Process, ProcessData


async def main(redis_url: str, method: str, process: Process):
    redis = aioredis.from_url(redis_url)
    pubsub = redis.pubsub()
    channel_name = f"process_method:{method}"
    await pubsub.subscribe(channel_name)
    try:
        async for message in pubsub.listen():
            if message["type"] != "message":
                continue

            data = json.loads(message["data"])
            model = ProcessData()
            model.id = data["id"]
            model.data_id = data["data_id"]
            model.url = data["url"]
            asyncio.create_task(process.run(model))
    except KeyboardInterrupt:
        pubsub.unsubscribe(channel_name)


def start(redis_url: str, method: str, process: Process):
    asyncio.run(main(redis_url, method, process))
