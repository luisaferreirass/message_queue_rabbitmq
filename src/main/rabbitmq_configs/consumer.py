import pika
import json


def rabbitmq_callback(ch, method, properties, body):
    msg = body.decode("utf-8")
    formatted_msg = json.loads(msg)
    # Transformando em dicionario
    print(formatted_msg["msg"])

    # Temos que tratar as mensagens que recebemos e fazemos isso com o callback



class RabbitMQConsumer:
    def __init__(self):
        self.__host = "localhost"
        self.__port = "5672"
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "minha_QUEUE"
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
        channel.queue_declare(
            queue=self.__queue,
            durable=True
        )
        # Declarando a queue na conexão

        channel.basic_consume(
            queue=self.__queue,
            auto_ack=True,
            # Mostrar que recebemos a mensagem
            on_message_callback=rabbitmq_callback
            # Se vc receber alguma mensagem nessa minha queue, vc vai
            # redirecionar para o callback
        )

        # Configurações básicas de consumo

        return channel

    def start(self):
        print("sistema conectado")
        self.__channel.start_consuming()

        # Quando der o start, vamos começar a ler as mesnagens
