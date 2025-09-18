# Use an existing image with Ubuntu or other Linux distros as a base
FROM ubuntu:latest

# Install dependencies and OpenJDK 25
RUN apt-get update && \
    apt-get install -y wget gnupg2 software-properties-common && \
    wget -qO - https://packages.openjdk.java.net/openjdk-25/KEY.asc | apt-key add - && \
    add-apt-repository "deb https://packages.openjdk.java.net/openjdk-25/ubuntu $(lsb_release -sc) main" && \
    apt-get update && \
    apt-get install -y openjdk-25-jdk

# Set the JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-25-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH
