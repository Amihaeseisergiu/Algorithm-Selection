FROM arm64v8/maven:3.8-amazoncorretto-19 AS build
COPY /src/process /process

RUN mvn install:install-file -Dfile=/process/dependencies/graph4j-1.0.1.jar -DgroupId=org.graph4j -DartifactId=graph4j \
     -Dversion=1.0.1 -Dpackaging=jar
RUN mvn -f /process/pom.xml compile assembly:single

FROM python:3.10
COPY --from=arm64v8/amazoncorretto:19 /usr/lib/jvm/java-19-amazon-corretto /usr/lib/jvm/java-19-amazon-corretto
COPY --from=build /process/target/process.jar /process/process.jar

ENV JAVA_HOME /usr/lib/jvm/java-19-amazon-corretto
RUN update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-19-amazon-corretto/bin/java 1

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV RABBITMQ_USER=user
ENV RABBITMQ_PASS=pass
ENV WEB_SERVICE_NAME=web-service
ENV INSTANCES_TOPIC=instances
ENV INSTANCES_QUEUE=graph4j_instances
ENV ALGORITHMS_TOPIC=algorithms
ENV LIBRARY_NAME=Graph4J

CMD python3 /app/src/service.py