import whisper
import tempfile
import os

model = whisper.load_model("base")

def transcribe_audio(uploaded_file):

    extension = uploaded_file.name.split(".")[-1]

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix="."+extension
    ) as tmp:

        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    result = model.transcribe(temp_path)

    os.remove(temp_path)

    return result["text"]