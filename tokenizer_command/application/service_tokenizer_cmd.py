from abc import ABC, abstractmethod
from tokenizer_command.application.dto_raw_data import MedicalRecordDTO
from tokenizer_command.domain.port_tokenizer_repo import ITokenizerRepository

class ITokenizerCmdService(ABC):
    @abstractmethod
    def tokenize(self, dto: MedicalRecordDTO) -> bool:
        pass

class TokenizerCmdService(ITokenizerCmdService):
    def __init__(self, repo: ITokenizerRepository):
        self.repo = repo

    def tokenize(self, dto: MedicalRecordDTO) -> bool:
        print("saving data...")
        medical_record = dto.to_entity()
        print("medical report: ", medical_record)
        self.repo.insert_record(medical_record)
        # self.tokenizer_port.query_event_emit(medical_record)
        return True