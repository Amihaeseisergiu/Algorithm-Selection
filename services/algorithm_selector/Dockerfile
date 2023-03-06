FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass
ENV INSTANCES_TOPIC=instances
ENV ALGORITHMS_TOPIC=algorithms
ENV ALGORITHMS_QUEUE=algorithms_responses

CMD python3 /src/service.py