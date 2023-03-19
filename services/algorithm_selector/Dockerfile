FROM python:3.10

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass
ENV WEB_SERVICE_NAME=web-service
ENV INSTANCES_TOPIC=instances
ENV INSTANCES_QUEUE=selectors_instances
ENV ALGORITHMS_TOPIC=algorithms
ENV ALGORITHMS_QUEUE=selectors_algorithms

CMD python3 /app/src/service.py