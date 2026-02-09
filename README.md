# 🐰 Message Queue RabbitMQ

## 📝 Sobre o projeto

Sistema de mensageria assíncrona desenvolvido com **RabbitMQ** e **Python**, implementando comunicação desacoplada entre serviços através de filas de mensagens com integração ao **Telegram**. O projeto demonstra conceitos de arquitetura baseada em eventos, processamento assíncrono e notificações em tempo real.

Ideal para aprendizado de:
- Message Queue (Filas de mensagens)
- RabbitMQ - Message broker
- Comunicação assíncrona entre serviços
- Padrões Publisher/Subscriber
- Arquitetura orientada a eventos
- Integração com Telegram Bot API
- Processamento paralelo de mensagens
- Microserviços desacoplados

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **RabbitMQ** - Message broker
- **Pika** - Cliente RabbitMQ para Python
- **Telegram Bot API** - Envio de notificações
- **Requests** - HTTP library

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- RabbitMQ instalado e rodando
- Bot do Telegram configurado
- pip (gerenciador de pacotes Python)

### Instalação do RabbitMQ

**Instalação Local:**
```bash
# Ubuntu/Debian
sudo apt-get install rabbitmq-server

# macOS
brew install rabbitmq

# Iniciar serviço
sudo service rabbitmq-server start
```

**Acessar o Management Console:**
- URL: `http://localhost:15672`
- Usuário: `guest`
- Senha: `guest`

### Configuração do Bot do Telegram

1. Crie um bot no Telegram:
   - Fale com [@BotFather](https://t.me/botfather)
   - Use o comando `/newbot`
   - Siga as instruções para criar seu bot
   - Copie o token fornecido

2. Obtenha o Chat ID:
   - Adicione o bot ao seu grupo/canal
   - Use [@userinfobot](https://t.me/userinfobot) para obter o chat_id

3. Configure as credenciais no código:
```python
# src/drivers/telegram_sender.py
token = "SEU_TOKEN_AQUI"
chat_id = "SEU_CHAT_ID_AQUI"
```

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luisaferreirass/message_queue_rabbitmq.git
cd message_queue_rabbitmq
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências

### Executando o Consumer (Consumidor)
```bash
python consumer.py
```

### Executando o Publisher (Produtor)
```bash
python publisher.py
```

## 🎯 Funcionalidades

- 📤 **Publisher**: Publica mensagens na fila RabbitMQ
- 📥 **Consumer**: Consome mensagens e processa callbacks
- 💬 **Telegram Integration**: Envia notificações automaticamente para o Telegram
- 🔄 **Exchange-based Routing**: Roteamento de mensagens via exchange
- ✅ **Auto Acknowledgment**: Confirmação automática de processamento
- 🔁 **Durable Queues**: Filas persistentes que sobrevivem a reinicializações
- 📨 **JSON Messages**: Mensagens estruturadas em formato JSON

## 🏗️ Arquitetura
```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│  Publisher  │ ──────> │  RabbitMQ   │ ──────> │  Consumer   │
│             │         │  Exchange   │         │             │
└─────────────┘         └──────┬──────┘         └──────┬──────┘
                               │                       │
                        ┌──────┴──────┐         ┌──────┴──────┐
                        │minha_queue2 │         │  Callback   │
                        │ (Messages)  │         │  Handler    │
                        └─────────────┘         └──────┬──────┘
                                                       │
                                                ┌──────┴──────┐
                                                │  Telegram   │
                                                │   Sender    │
                                                └─────────────┘
```

## 📮 Componentes do Sistema

### 1. Publisher (Produtor)
- Publica mensagens no exchange `minha_exchange`
- Converte mensagens para formato JSON
- Configuração de delivery mode persistente
- Credenciais: `guest/guest` em `localhost:5672`

### 2. Consumer (Consumidor)
- Escuta a fila `minha_queue2`
- Binding com routing key `1`
- Auto-acknowledgment habilitado
- Redireciona mensagens para callback

### 3. Callback Handler
- Decodifica mensagens JSON
- Extrai o campo `msg`
- Envia para o Telegram Sender

### 4. Telegram Sender
- Envia mensagens via Telegram Bot API
- Suporta grupos e canais
- Integração com bot configurado

## 💡 Exemplos de uso

### Publicar uma mensagem
```python
from src.infra.rabbitmq_publisher import RabbitMQPublisher

# Criar publisher
publisher = RabbitMQPublisher()

# Enviar mensagem
message = {
    "msg": "🚀 Nova notificação do sistema!"
}

publisher.send_message(message)
print("Mensagem enviada para a fila!")
```

### Consumir mensagens
```python
from src.infra.rabbitmq_consumer import RabbitMQConsumer

# Criar consumer
consumer = RabbitMQConsumer()

# Iniciar consumo
consumer.start()
# Output: "sistema conectado"
# Aguardando mensagens...
```

### Fluxo completo
```python
# 1. Publisher envia mensagem
message_body = {
    "msg": "Pedido #1234 foi processado com sucesso!"
}
publisher.send_message(message_body)

# 2. RabbitMQ roteia para a fila

# 3. Consumer recebe e processa

# 4. Callback extrai a mensagem

# 5. Telegram envia notificação para o grupo/canal
```

## 📊 Casos de Uso

### 1. Notificações de Sistema
```
Sistema gera alerta → Fila → Telegram notifica administradores
```

### 2. Alertas de Erro
```
Aplicação detecta erro → Fila → Equipe recebe notificação imediata
```

### 3. Status de Pedidos
```
Pedido atualizado → Fila → Cliente recebe atualização no Telegram
```

### 4. Monitoramento
```
Métricas coletadas → Fila → Dashboard e alertas no Telegram
```

### 5. Workflows Automatizados
```
Evento disparado → Fila → Múltiplas ações (DB, Email, Telegram)
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
