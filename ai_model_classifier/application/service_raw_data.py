from abc import ABC, abstractmethod
from ai_model_classifier.domain.model_raw_data import RawData
from ai_model_classifier.domain.port_tokenizer import TokenizerPort

class IRawDataService(ABC):
    @abstractmethod
    def send_raw_data(self, raw_data: RawData) -> dict:
        pass

class RawDataService(IRawDataService):
    def __init__(self, tokenizer: TokenizerPort):
        self.tokenizer = tokenizer

    def send_raw_data(self, raw_data: RawData) -> dict:
        try:
            self.tokenizer.tokenize(raw_data)
        except Exception as e:
            return {"status": "error", "message": str(e)}

        return {"status": "success", "message": "Raw data event emitted successfully"}