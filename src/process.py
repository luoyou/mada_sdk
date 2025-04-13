from abc import ABC, abstractmethod


class ProcessData:
    id: int
    data_id: int
    url: str


class Process(ABC):

    @abstractmethod
    async def run(self, data: ProcessData): ...
