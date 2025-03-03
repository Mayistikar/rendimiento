from tokenizer_command.infrastructure.pulsar.consumer import Consumer, Config
from tokenizer_command.application.service_tokenizer_cmd import TokenizerCmdService
from tokenizer_command.infrastructure.db.adapter_tokenizer_repo_mysql import TokenizerRepository

if __name__ == '__main__':
        '''
        tokenizer_query_config = Config(
            service_url='pulsar://localhost:6650',
            topic='tokenizer_query',
            subscription='tokenizer_query'
        )
        tokenizer_query_adapter = TokenizerAdapterQuery(tokenizer_query_config)
        '''

        tokenizer_repository = TokenizerRepository()
        tokenizer_service = TokenizerCmdService(tokenizer_repository)
        tokenizer_cmd_config = Config(
            service_url='pulsar://localhost:6650',
            topic='tokenizer_command',
            subscription='tokenizer_command'
        )
        subscriber = Consumer(tokenizer_cmd_config, tokenizer_service)
        subscriber.run()