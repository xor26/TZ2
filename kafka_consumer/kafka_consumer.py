from kafka import KafkaConsumer
from json import loads
import redis
from configs.config import RedisConfig
from configs.config import KafkaConfig


consumer = KafkaConsumer(
    "files",
    bootstrap_servers=[f"{KafkaConfig.KAFKA_HOST_NAME}:{KafkaConfig.KAFKA_HOST_PORT}"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="my-group",
    value_deserializer=lambda x: loads(x.decode("utf-8")))

db = redis.Redis(host=RedisConfig.KAFKA_HOST_NAME, port=RedisConfig.KAFKA_HOST_PORT)

print("Starting...")

for message in consumer:
    message = message.value
    db.mset({message["file_name"]: message["file_path"]})

    print("Received: " + str(message))
    print("Stored: " + str(db.get(message["file_name"])
                           ))
