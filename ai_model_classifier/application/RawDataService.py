from abc import ABC, abstractmethod
from domain.RawData import RawData

class IRawDataService(ABC):
    @abstractmethod
    def send_raw_data(self, raw_data: RawData) -> dict:
        pass

class RawDataService(IRawDataService):
    def send_raw_data(self, raw_data: RawData) -> dict:
        return {"status": "success", "message": "Raw data event emitted successfully"}