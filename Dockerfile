# Use an existing image with Ubuntu or other Linux distros as a base
FROM ubuntu:latest

# Install dependencies and OpenJDK 25
RUN mkdir -p /usr/lib/jvm
RUN apt-get update && apt-get install wget
RUN wget https://download.java.net/java/GA/jdk25/bd75d5f9689641da8e1daabeccb5528b/36/GPL/openjdk-25_linux-aarch64_bin.tar.gz 
RUN tar -zxf openjdk-25*_bin.tar.gz -C /usr/lib/jvm/
RUN update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-25/bin/java 1
RUN update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-25/bin/javac 1

# Set the JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-25-openjdk-amd64
ENV PATH $JAVA_HOME/bin:$PATH
