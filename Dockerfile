# Base image
FROM openjdk:8-jre-slim

# Set environment variables
ENV SPARK_VERSION=3.2.4
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/spark

# Install Python 3.7.16 and pip
RUN apt-get update && apt-get install -y python3.7 python3.7-distutils && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1 && \
    wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    rm get-pip.py && apt-get clean

# Download and install Spark
RUN wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xvf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME} && \
    rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Copy spark-defaults.conf.template and configure
COPY spark-defaults.conf.template ${SPARK_HOME}/conf/spark-defaults.conf.template
RUN sed -i 's/# spark\.master\..*/spark\.master\..*/' ${SPARK_HOME}/conf/spark-defaults.conf.template && \
    sed -i 's/# spark\.serializer\..*/spark\.serializer\..*/' ${SPARK_HOME}/conf/spark-defaults.conf.template

# Export SPARK_HOME environment variable
ENV PATH=${PATH}:${SPARK_HOME}/bin

