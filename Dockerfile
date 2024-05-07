FROM python:3.12-bullseye
WORKDIR /app

RUN sudo apt update && sudo apt upgrade -y
RUN sudo apt install -y libffi-dev ffmpeg libnacl-dev python3-dev python3-pyaudio

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY bot.py bot.py

CMD ["python", "bot.py"]