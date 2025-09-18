FROM jupyter/minimal-notebook:latest
USER root

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh

# Install Node.js 18.x and npm, required for many Jupyter extensions
RUN apt-get update && apt-get install -yq curl gnupg ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -yq nodejs

# Install OpenJDK 25 from Adoptium
RUN mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://packages.adoptium.net/artifactory/api/gpg/key/public | tee /etc/apt/keyrings/adoptium.asc \
    && echo "deb [signed-by=/etc/apt/keyrings/adoptium.asc] https://packages.adoptium.net/artifactory/deb $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/adoptium.list \
    && apt-get update \
    && apt-get install -y temurin-25-jdk \
    && java -version

# Install Python/Jupyter extensions
RUN pip install matplotlib jupyterlab-myst jupyter-book 'jupyterlab_pygments==0.3.0' ipywidgets tldraw ipyflex jupyter_nbextensions_configurator jupyter_contrib_nbextensions 'ipysheet==0.7.0' 'ipysketch-lite==0.4.2' qgridnext Pillow 'marimo>=0.6.21' jupyter-marimo-proxy nbgitpuller jupyterlab-git aquirdturtle_collapsible_headings ipydatagrid ipydrawio ipydrawio-export jupyterlab_rise jupyter-code-server jupyter-server-proxy
# RUN pip install jupyter-wysiwyg

# Install VS Code extensions
RUN code-server --install-extension ms-python.python \
    && code-server --install-extension ms-toolsai.jupyter \
    && code-server --install-extension formulahendry.code-runner \
    && code-server --install-extension vscjava.vscode-java-pack

# Build JupyterLab
RUN jupyter lab build

# Switch back to non-root user
USER $NB_USER
