from ai_model_classifier.domain.model_raw_data import RawData
from ai_model_classifier.domain.port_tokenizer import TokenizerPort
import pulsar
import json

class TokenizerAdapter(TokenizerPort):
    def __init__(self, pulsar_client: pulsar.Client):
        self.pulsar_client = pulsar_client

    def tokenize(self, raw_data: RawData) -> bool:
        try:
            producer = self.pulsar_client.create_producer('tokenizer_command')
            producer.send(json.dumps(raw_data.to_json()).encode('utf-8'))
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
