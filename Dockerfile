FROM jupyter/base-notebook:latest
USER root
RUN apt-get update && apt-get install -yq curl
RUN curl -fsSL https://code-server.dev/install.sh | sh

RUN pip install jupyter-code-server jupyter-server-proxy

# Set environment variables for Java 25
ENV JAVA_HOME=/opt/jdk-25
ENV PATH="$JAVA_HOME/bin:$PATH"

# Download and install OpenJDK 25
RUN apt-get update && apt-get install -y --no-install-recommends wget \
    && mkdir -p /opt \
    && wget -O /tmp/openjdk.tar.gz https://download.java.net/java/GA/jdk25/bd75d5f9689641da8e1daabeccb5528b/36/GPL/openjdk-25_linux-x64_bin.tar.gz \
    && tar -zxvf /tmp/openjdk.tar.gz -C /opt \
    && rm /tmp/openjdk.tar.gz \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip > ijava-kernel.zip

# Unpack and install the kernel
RUN unzip ijava-kernel.zip -d ijava-kernel \
  && cd ijava-kernel \
  && python3 install.py --sys-prefix

ENV CODE_DISABLE_PASSWORD="True"

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-toolsai.jupyter
RUN code-server --install-extension formulahendry.code-runner
RUN code-server --install-extension vscjava.vscode-java-pack

RUN jupyter lab build

# Switch back to the non-root user
USER $NB_USER