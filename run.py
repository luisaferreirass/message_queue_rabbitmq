from src.main.rabbitmq_configs.consumer import RabbitMQConsumer
from src.main.rabbitmq_configs.publisher import RabbitMQPublisher


if __name__ == "__main__":

    publisher = RabbitMQPublisher()
    publisher.send_message({ "msg": "outra nova mensagem" })
    consumer = RabbitMQConsumer()
    consumer.start()
