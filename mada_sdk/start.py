import asyncio
import json
import httpx
from redis import asyncio as aioredis

from .process import Process, ProcessData, ProcessResult


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
            bg_task = asyncio.create_task(process.run(model))
            bg_task.add_done_callback(lambda t: t.result())  # Handle exceptions if needed
    except KeyboardInterrupt:
        pubsub.unsubscribe(channel_name)


def done_callback(result: ProcessResult):
    print(f"Process completed with result: {result: ProcessResult.content} of type {result: ProcessResult.file_type}")


async def get_process_data(uuid: int) -> ProcessData:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://label.madacode.com/openapi/process/{uuid}")
        if response.status_code == 200:
            return ProcessData(**response.json())
        else:
            raise Exception(f"Error fetching process data: {response.status_code}")


def start(redis_url: str, method: str, process: Process):
    asyncio.run(main(redis_url, method, process))
