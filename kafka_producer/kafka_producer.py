from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["kafka:9092"],
    value_serializer=lambda x:
    dumps(x).encode("utf-8")
)
print("started....")

for e in range(1000):
    data = {"number": e}
    producer.send("files", value=data)
    print("Sended " + str(e))
    sleep(5)
