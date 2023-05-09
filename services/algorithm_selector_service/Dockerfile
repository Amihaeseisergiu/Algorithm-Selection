FROM python:3.10

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass

ENV WEAVIATE_HOST_NAME=weaviate

ENV DATASET_ENTRY_TOPIC=dataset_entry
ENV DATASET_ENTRY_QUEUE=dataset_entry_selectors

ENV USER_ALGORITHM_TOPIC=user_algorithm
ENV INSTANCES_TOPIC=instances
ENV INSTANCES_QUEUE=selector_instances
ENV INSTANCES_KEY=instances.selector

ENV MAJORITY_VOTING_DATAPOINTS=10

CMD python3 /app/src/service.py