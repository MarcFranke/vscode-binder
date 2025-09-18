FROM jupyter/minimal-notebook:latest
USER root

ENV CODESERVER_URL="https://github.com/cdr/code-server/releases/download/1.1119-vsc1.33.1/code-server1.1119-vsc1.33.1-linux-x64.tar.gz" \
    CODESERVER="code-server1.1119-vsc1.33.1-linux-x64"

RUN wget ${CODESERVER_URL} && \
    tar xvf ${CODESERVER}.tar.gz && \
    mv ${CODESERVER}/code-server /usr/local/bin/ && \
    rm -rf code-server* && \
    rm -rf /tmp/* && \
    rm -rf $HOME/.cache && \
    rm -rf $HOME/.node-gyp

# Install Node.js 18.x and npm, die für viele Jupyter-Erweiterungen erforderlich sind
RUN apt-get update && apt-get install -yq curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -yq nodejs

RUN pip install matplotlib jupyterlab-myst jupyter-book 'jupyterlab_pygments==0.3.0' ipywidgets tldraw ipyflex jupyter_nbextensions_configurator jupyter_contrib_nbextensions 'ipysheet==0.7.0' 'ipysketch-lite==0.4.2' qgridnext Pillow 'marimo>=0.6.21' jupyter-marimo-proxy nbgitpuller jupyterlab-git aquirdturtle_collapsible_headings ipydatagrid ipydrawio ipydrawio-export jupyterlab_rise jupyter-code-server jupyter-server-proxy
# RUN pip install jupyter-wysiwyg

#RUN code-server --install-extension ms-python.python
#RUN code-server --install-extension ms-toolsai.jupyter
#RUN code-server --install-extension formulahendry.code-runner

RUN jupyter lab build

# Zurückschalten zum Nicht-Root-Benutzer
USER $NB_USER


