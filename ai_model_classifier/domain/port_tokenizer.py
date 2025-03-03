from abc import ABC, abstractmethod
from ai_model_classifier.domain.model_raw_data import RawData

class TokenizerPort(ABC):
    @abstractmethod
    def tokenize(self, raw_data: RawData) -> bool:
        pass
