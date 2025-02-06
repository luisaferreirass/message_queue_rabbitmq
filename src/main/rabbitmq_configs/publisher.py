import pika
import json

class RabbitMQPublisher:
    def __init__(self):
        self.__host = "localhost"
        self.__port = "5672"
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = "minha_exchange"
        self.__routing_key = ""
        self.__channel = self.create_channel()
        # Qunado instanciar um objeto dessa classe, já vai criar um channel

        # O channel vai se conectar c o rabbit

    def create_channel(self) -> None:
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )

        )

        # Colocamos os parametros aqui

        channel = pika.BlockingConnection(connection_parameters).channel()
        # Estamos criando o channel

        return channel

    def send_message(self, body: dict) -> None:
        self.__channel.basic_publish(
            exchange= self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            # Estamos transformand o body em uma string json
            properties=pika.BasicProperties(
                delivery_mode=2
                # Modo de entrega padrão
            )
        )