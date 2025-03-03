from abc import ABC, abstractmethod
from tokenizer_query.application.dto_raw_data import MedicalRecordDTO
from tokenizer_query.domain.port_tokenizer_repo import ITokenizerRepository

class ITokenizerQueryService(ABC):
    @abstractmethod
    def tokenize(self, dto: MedicalRecordDTO) -> bool:
        pass

class TokenizerQueryService(ITokenizerQueryService):
    def __init__(self, repo: ITokenizerRepository):
        self.repo = repo

    def tokenize(self, dto: MedicalRecordDTO) -> bool:
        print("saving data to tokenizer query db...")
        medical_record = dto.to_entity()
        self.repo.insert_record(medical_record)
        # self.tokenizer_port.query_event_emit(medical_record)
        return True