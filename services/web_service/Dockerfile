FROM node:19.7-alpine AS node

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run css

FROM python:3.10

WORKDIR /app
COPY . .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --from=node src/frontend/static/css src/frontend/static/css

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass
ENV USER_METRICS_TOPIC=user_metrics
ENV INSTANCES_TOPIC=instances
ENV INSTANCES_PARALLEL_KEY_PREFIX=instances.parallel
ENV INSTANCES_SEQUENTIAL_KEY_PREFIX=instances.sequential
ENV LIBRARY_NAMES=NetworkX,Graph4J,JGraphT
ENV SEQUENTIAL_LIBRARY_NAMES=networkx,graph4j,jgrapht
ENV NEXT_LIBRARY_TOPIC=next_library

CMD python3 /app/src/backend/service.py