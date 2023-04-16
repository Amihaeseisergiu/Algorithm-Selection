FROM python:3.10

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass

CMD python3 /app/src/service.py