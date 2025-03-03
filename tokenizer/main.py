from tokenizer.infrastructure.pulsar.consumer import Consumer, Config

if __name__ == '__main__':

        config = Config(
            service_url='pulsar://localhost:6650',
            topic='tokenizer',
            subscription='tokenizer'
        )

        subscriber = Consumer(config)
        subscriber.run()