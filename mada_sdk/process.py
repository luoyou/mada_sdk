from abc import ABC, abstractmethod
from enum import StrEnum


class ProcessData:
    id: int
    data_id: int
    url: str


class FileType(StrEnum):
    file = "file"
    text = "text"


class ProcessResult:
    id: int
    file_type: FileType
    content: str


class Process(ABC):
    @abstractmethod
    async def run(self, data: ProcessData) -> ProcessResult: ...
