from abc import ABC, abstractmethod
from tokenizer_command.domain.model_tokenized_data import MedicalRecord

class TokenizerPort(ABC):
    @abstractmethod
    def query_event_emit(self, tokenized_data: MedicalRecord) -> bool:
        pass
