FROM python:3.10

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

# Service variables
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass
ENV WEB_SERVICE_NAME=web-service
ENV INSTANCES_TOPIC=instances
ENV INSTANCES_QUEUE=networkx_instances
ENV USER_METRICS_TOPIC=user_metrics
ENV SELECTOR_METRICS_TOPIC=selector_metrics
ENV LIBRARY_NAME=NetworkX

# Process variables
ENV SELECTOR_ALGORITHMS_TOPIC=selector_algorithms

CMD python3 /app/src/service.py