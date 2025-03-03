from ai_model_classifier.infrastructure.pulsar.adapter_tokenizer import TokenizerAdapter
from infrastructure.http.server import Server
from infrastructure.http.routes import Routes
from application.service_raw_data import RawDataService
import pulsar

if __name__ == "__main__":
    pulsar_client = pulsar.Client('pulsar://localhost:6650')
    tokenizer = TokenizerAdapter(pulsar_client)
    raw_data_service = RawDataService(tokenizer)

    router = Routes(raw_data_service).router
    server = Server([router])

    # Run the server
    server.run(host="0.0.0.0", port=8000)