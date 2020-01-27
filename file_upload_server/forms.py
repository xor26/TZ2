from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import FileField, SubmitField


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[
        FileRequired(),
    ])
    submit = SubmitField("Upload")
