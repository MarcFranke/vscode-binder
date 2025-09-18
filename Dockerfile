FROM jupyter/minimal-notebook:latest
USER root

RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Node.js 18.x and npm, which are required for many Jupyter extensions
RUN apt-get update && apt-get install -yq curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -yq nodejs

# Set environment variables for Java 25
ENV JAVA_HOME=/opt/jdk-25
ENV PATH="$JAVA_HOME/bin:$PATH"

# Download and install OpenJDK 25
RUN apt-get update && apt-get install -y --no-install-recommends wget \
    && mkdir -p /opt \
    && wget -O /tmp/openjdk.tar.gz https://download.java.net/java/early_access/jdk25/3/GPL/openjdk-25_linux-x64_bin.tar.gz \
    && tar -zxvf /tmp/openjdk.tar.gz -C /opt \
    && rm /tmp/openjdk.tar.gz \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install matplotlib jupyterlab-myst jupyter-book 'jupyterlab_pygments==0.3.0' ipywidgets tldraw ipyflex jupyter_nbextensions_configurator jupyter_contrib_nbextensions 'ipysheet==0.7.0' 'ipysketch-lite==0.4.2' qgridnext Pillow 'marimo>=0.6.21' jupyter-marimo-proxy nbgitpuller jupyterlab-git aquirdturtle_collapsible_headings ipydatagrid ipydrawio ipydrawio-export jupyterlab_rise jupyter-code-server jupyter-server-proxy
# RUN pip install jupyter-wysiwyg

RUN code-server --install-extension ms-python.python
RUN code-server --install-extension ms-toolsai.jupyter
RUN code-server --install-extension formulahendry.code-runner
RUN code-server --install-extension vscjava.vscode-java-pack

RUN jupyter lab build

# Switch back to the non-root user
USER $NB_USER