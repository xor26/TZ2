import os
import time
from json import dumps
from flask import Flask, render_template, request, redirect
from kafka import KafkaProducer
from forms import UploadFileForm
from configs.config import FlaskConfig
from configs.config import KafkaConfig

app = Flask(__name__)
app.config.from_object(FlaskConfig)
kafka_producer = KafkaProducer(bootstrap_servers=[f"{KafkaConfig.KAFKA_HOST_NAME}:{KafkaConfig.KAFKA_HOST_PORT}"],
                               value_serializer=lambda x:
                               dumps(x).encode("utf-8"))


@app.route("/", methods=["GET"])
def user_add_form_request():
    form = UploadFileForm()
    return render_template("upload_file.html", title="New file", form=form)


@app.route("/", methods=["POST"])
def user_add_form_send():
    file = request.files["file"]
    file_format = file.filename.split('.')[-1]
    new_file_name = str(time.time()).replace(".", "")
    new_file_name = f"{new_file_name}.{file_format}"
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], new_file_name)
    file.save(file_path)
    kafka_producer.send("files", value={"file_name": new_file_name, "file_path": file_path})
    print("sended")

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
