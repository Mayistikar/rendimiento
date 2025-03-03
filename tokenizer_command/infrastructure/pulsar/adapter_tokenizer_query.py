import pulsar
import json
from tokenizer_command.domain.port_tokenizer_query import TokenizerPort
from tokenizer_command.domain.model_tokenized_data import MedicalRecord
from tokenizer_command.infrastructure.pulsar.consumer import Config


class TokenizerAdapterQuery(TokenizerPort):
    def __init__(self, config: Config):
        self.client = pulsar.Client(config.service_url)

    def query_event_emit(self, tokenized_data: MedicalRecord) -> bool:
        try:
            producer = self.pulsar_client.create_producer('tokenizer_query')
            producer.send(json.dumps(tokenized_data).encode('utf-8'))
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
