FROM python:3.8

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY ./ /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
