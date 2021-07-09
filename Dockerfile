FROM debian:latest

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y ffmpeg python3-pip curl
RUN python3 -m pip install -U pip

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

COPY . .

RUN python3 -m pip install -U -r requirements.txt

CMD ["python3", "main.py"]
