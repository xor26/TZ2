import os


class FlaskConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "xxx"
    UPLOAD_FOLDER = os.environ.get("FILE_DIR") or "file_storage/"


class KafkaConfig:
    KAFKA_HOST_NAME = os.environ.get("KAFKA_HOST_NAME") or "localhost"
    KAFKA_HOST_PORT = os.environ.get("KAFKA_HOST_PORT") or "9092"


class RedisConfig:
    KAFKA_HOST_NAME = os.environ.get("REDIS_HOST_NAME") or "localhost"
    KAFKA_HOST_PORT = os.environ.get("REDIS_HOST_PORT") or "6379"
