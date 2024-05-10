FROM python:3.12-bullseye as dev
RUN apt update && apt upgrade -y
RUN apt install -y libffi-dev ffmpeg libnacl-dev python3-dev python3-pyaudio

FROM dev as prod
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY bot.py bot.py

CMD ["python", "bot.py"]