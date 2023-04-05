FROM arm64v8/maven:3.9.0-amazoncorretto-19 AS build
COPY /src/process /process
RUN mvn -f /process/pom.xml compile assembly:single

FROM python:3.10
COPY --from=arm64v8/amazoncorretto:19 /usr/lib/jvm/java-19-amazon-corretto /usr/lib/jvm/java-19-amazon-corretto
COPY --from=build /process/target/process.jar /process/process.jar

ENV JAVA_HOME /usr/lib/jvm/java-19-amazon-corretto
RUN update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-19-amazon-corretto/bin/java 1

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
ENV INSTANCES_QUEUE=jgrapht_instances
ENV USER_METRICS_TOPIC=user_metrics
ENV SELECTOR_METRICS_TOPIC=selector_metrics
ENV LIBRARY_NAME=JGraphT

CMD python3 /app/src/service.py