# 🐰 Message Queue RabbitMQ

## 📝 About the project

Asynchronous messaging system built with **RabbitMQ** and **Python**, implementing decoupled communication between services through message queues, integrated with **Telegram**. The project demonstrates concepts of event-driven architecture, asynchronous processing and real-time notifications.

Great for learning:
- Message Queues
- RabbitMQ - Message broker
- Asynchronous communication between services
- Publisher/Subscriber patterns
- Event-driven architecture
- Telegram Bot API integration
- Parallel message processing
- Decoupled microservices

## 🚀 Technologies used

- **Python 3.x**
- **RabbitMQ** - Message broker
- **Pika** - RabbitMQ client for Python
- **Telegram Bot API** - Sending notifications
- **Requests** - HTTP library

## ⚙️ How to run

### Prerequisites

- Python 3.x installed
- RabbitMQ installed and running
- A configured Telegram bot
- pip (Python package manager)

### Installing RabbitMQ

**Local installation:**
```bash
# Ubuntu/Debian
sudo apt-get install rabbitmq-server

# macOS
brew install rabbitmq

# Start the service
sudo service rabbitmq-server start
```

**Access the Management Console:**
- URL: `http://localhost:15672`
- Username: `guest`
- Password: `guest`

### Telegram Bot Setup

1. Create a Telegram bot:
   - Talk to [@BotFather](https://t.me/botfather)
   - Use the `/newbot` command
   - Follow the instructions to create your bot
   - Copy the token provided

2. Get the Chat ID:
   - Add the bot to your group/channel
   - Use [@userinfobot](https://t.me/userinfobot) to get the chat_id

3. Set the credentials in the code:
```python
# src/drivers/telegram_sender.py
token = "YOUR_TOKEN_HERE"
chat_id = "YOUR_CHAT_ID_HERE"
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/luisaferreirass/message_queue_rabbitmq.git
cd message_queue_rabbitmq
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install the dependencies

### Running the Consumer
```bash
python consumer.py
```

### Running the Publisher
```bash
python publisher.py
```

## 🎯 Features

- 📤 **Publisher**: Publishes messages to the RabbitMQ queue
- 📥 **Consumer**: Consumes messages and runs callbacks
- 💬 **Telegram Integration**: Automatically sends notifications to Telegram
- 🔄 **Exchange-based Routing**: Message routing through an exchange
- ✅ **Auto Acknowledgment**: Automatic processing acknowledgment
- 🔁 **Durable Queues**: Persistent queues that survive restarts
- 📨 **JSON Messages**: Structured messages in JSON format

## 🏗️ Architecture
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

## 📮 System Components

### 1. Publisher (Producer)
- Publishes messages to the `minha_exchange` exchange
- Converts messages to JSON format
- Persistent delivery mode configuration
- Credentials: `guest/guest` at `localhost:5672`

### 2. Consumer
- Listens to the `minha_queue2` queue
- Binding with routing key `1`
- Auto-acknowledgment enabled
- Forwards messages to the callback

### 3. Callback Handler
- Decodes JSON messages
- Extracts the `msg` field
- Sends it to the Telegram Sender

### 4. Telegram Sender
- Sends messages through the Telegram Bot API
- Supports groups and channels
- Integration with the configured bot

## 💡 Usage examples

### Publish a message
```python
from src.infra.rabbitmq_publisher import RabbitMQPublisher

# Create the publisher
publisher = RabbitMQPublisher()

# Send a message
message = {
    "msg": "🚀 New system notification!"
}

publisher.send_message(message)
print("Message sent to the queue!")
```

### Consume messages
```python
from src.infra.rabbitmq_consumer import RabbitMQConsumer

# Create the consumer
consumer = RabbitMQConsumer()

# Start consuming
consumer.start()
# Output: "sistema conectado" (system connected)
# Waiting for messages...
```

### Complete flow
```python
# 1. Publisher sends a message
message_body = {
    "msg": "Order #1234 was processed successfully!"
}
publisher.send_message(message_body)

# 2. RabbitMQ routes it to the queue

# 3. Consumer receives and processes it

# 4. Callback extracts the message

# 5. Telegram sends the notification to the group/channel
```

## 📊 Use Cases

### 1. System Notifications
```
System raises an alert → Queue → Telegram notifies administrators
```

### 2. Error Alerts
```
Application detects an error → Queue → Team gets an immediate notification
```

### 3. Order Status
```
Order updated → Queue → Customer receives an update on Telegram
```

### 4. Monitoring
```
Metrics collected → Queue → Dashboard and Telegram alerts
```

### 5. Automated Workflows
```
Event triggered → Queue → Multiple actions (DB, Email, Telegram)
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👩‍💻 Author

Developed by [Luisa Ferreira](https://github.com/luisaferreirass)
