import pulsar

class Config:
    def __init__(self, service_url='pulsar://localhost:6650', topic='tokenizer', subscription='tokenizer'):
        self.service_url = service_url
        self.topic = topic
        self.subscription = subscription

class Consumer:
    def __init__(self, config: Config):
        self.service_url = config.service_url
        self.topic = config.topic
        self.subscription = config.subscription
        self.client = pulsar.Client(self.service_url)
        self.consumer = self.client.subscribe(self.topic, subscription_name=self.subscription)
        self.running = True

    def process_message(self, message):
        try:
            data = message.data().decode('utf-8')
            print("Mensaje recibido: '%s'" % data)
            self.consumer.acknowledge(message)
        except Exception as e:
            print("Error procesando el mensaje:", e)
            self.consumer.negative_acknowledge(message)

    def run(self):
        try:
            while self.running:
                msg = self.consumer.receive()
                self.process_message(msg)
        except KeyboardInterrupt:
            print("Interrupción recibida, deteniendo el consumidor...")
        finally:
            self.close()

    def close(self):
        self.running = False
        self.client.close()
        print("Cliente de Pulsar cerrado.")
