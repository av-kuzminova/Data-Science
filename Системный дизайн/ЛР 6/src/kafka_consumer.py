from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "emails",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="email-service-group",
)

def consume_events():
    for message in consumer:
        event = message.value
        print(f"Consumed event: {event}")
        # Здесь можно добавить логику для записи события в базу данных