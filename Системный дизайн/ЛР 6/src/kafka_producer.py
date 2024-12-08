from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

def publish_event(topic: str, event: dict):
    producer.send(topic, value=event)
    producer.flush()