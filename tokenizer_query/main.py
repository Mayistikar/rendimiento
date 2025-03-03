from tokenizer_query.infrastructure.pulsar.consumer import Consumer, Config
from tokenizer_query.application.service_tokenizer_query import TokenizerQueryService
from tokenizer_query.infrastructure.db.adapter_tokenizer_repo_mysql import TokenizerRepository

if __name__ == '__main__':
        tokenizer_repository = TokenizerRepository()
        tokenizer_service = TokenizerQueryService(tokenizer_repository)
        tokenizer_query_config = Config(
            service_url='pulsar://localhost:6650',
            topic='tokenizer_query',
            subscription='tokenizer_query'
        )
        subscriber = Consumer(tokenizer_query_config, tokenizer_service)
        subscriber.run()