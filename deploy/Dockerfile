FROM python:3.7-slim

RUN apt update && apt install git g++ -y

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

RUN mkdir /app
COPY app /app

WORKDIR /
COPY main.py .

CMD ["python", "main.py"]
