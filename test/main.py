from mada_sdk import start
from mada_sdk import Process, ProcessData


class Slice(Process):
    async def run(self, data: ProcessData):
        print(data.id)
        print(data.data_id)
        print(data.url)


if __name__ == "__main__":
    process = Slice()
    start("redis://localhost:6379", "test", process)
