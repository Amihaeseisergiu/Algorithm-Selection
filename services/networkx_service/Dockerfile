FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass
ENV ALGORITHM_SELECTOR_INSTANCES_TOPIC=algorithm_selectors_sent_instances
ENV ALGORITHM_SELECTOR_INSTANCES_QUEUE=networkx_received_instances
ENV ALGORITHMS_TOPIC=algorithms_sent_responses

CMD python3 /src/service.py