FROM python:3.10

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV LIBRARY_NAME=NetworkX

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass

ENV INSTANCES_TOPIC=instances
ENV INSTANCES_PARALLEL_QUEUE=networkx_instances_parallel
ENV INSTANCES_PARALLEL_KEY=instances.parallel
ENV INSTANCES_SEQUENTIAL_QUEUE=networkx_instances_sequential
ENV INSTANCES_SEQUENTIAL_KEY=instances.sequential.networkx

ENV USER_METRICS_TOPIC=user_metrics
ENV NEXT_LIBRARY_TOPIC=next_library

ENV DATA_AGGREGATOR_TOPIC=data_aggregator
ENV ALGORITHMS_DATA_KEY=algorithms.data
ENV INSTANCE_FEATURES_KEY=instance.features

ENV ALGORITHM_TIMEOUT=20

CMD python3 /app/src/service.py