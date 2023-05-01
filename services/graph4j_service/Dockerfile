FROM arm64v8/maven:3.8-amazoncorretto-19 AS build
COPY /src/process /process

RUN mvn install:install-file -Dfile=/process/dependencies/graph4j-1.0.3.jar -DgroupId=org.graph4j -DartifactId=graph4j \
     -Dversion=1.0.3 -Dpackaging=jar
RUN mvn -f /process/pom.xml compile assembly:single

FROM python:3.10
COPY --from=arm64v8/amazoncorretto:19 /usr/lib/jvm/java-19-amazon-corretto /usr/lib/jvm/java-19-amazon-corretto
COPY --from=build /process/target/process.jar /process/process.jar

ENV JAVA_HOME /usr/lib/jvm/java-19-amazon-corretto
RUN update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-19-amazon-corretto/bin/java 1

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV LIBRARY_NAME=Graph4J

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass

ENV INSTANCES_TOPIC=instances
ENV INSTANCES_PARALLEL_QUEUE=graph4j_instances_parallel
ENV INSTANCES_PARALLEL_KEY=instances.parallel
ENV INSTANCES_SEQUENTIAL_QUEUE=graph4j_instances_sequential
ENV INSTANCES_SEQUENTIAL_KEY=instances.sequential.graph4j

ENV USER_METRICS_TOPIC=user_metrics
ENV NEXT_LIBRARY_TOPIC=next_library

ENV DATA_AGGREGATOR_TOPIC=data_aggregator
ENV ALGORITHMS_DATA_KEY=algorithms.data
ENV INSTANCE_FEATURES_KEY=instance.features

CMD python3 /app/src/service.py