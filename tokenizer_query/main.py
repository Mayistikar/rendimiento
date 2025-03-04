# tokenizer_query/main.py
from tokenizer_query.infrastructure.pulsar.consumer import Consumer, Config
from tokenizer_query.application.service_tokenizer_query import TokenizerQueryService
from tokenizer_query.infrastructure.db.adapter_tokenizer_repo_mysql import TokenizerRepository
from tokenizer_query.infrastructure.http.server import ServerHTTP
import threading
import time


def run_consumer():
    tokenizer_repository = TokenizerRepository()
    tokenizer_service = TokenizerQueryService(tokenizer_repository)
    tokenizer_query_config = Config(
        service_url='pulsar://localhost:6650',
        topic='tokenizer_query',
        subscription='tokenizer_query'
    )
    subscriber = Consumer(tokenizer_query_config, tokenizer_service)
    subscriber.run()


def run_fastapi_server():
    repository = TokenizerRepository()
    server = ServerHTTP(repository)
    server.run(host="0.0.0.0", port=8001)


if __name__ == '__main__':
    # Start consumer in a separate thread
    consumer_thread = threading.Thread(target=run_consumer)
    consumer_thread.daemon = True
    consumer_thread.start()

    # Start FastAPI in another separate thread
    api_thread = threading.Thread(target=run_fastapi_server)
    api_thread.daemon = True
    api_thread.start()

    # Keep the main thread alive to manage the other threads
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Service shutting down...")