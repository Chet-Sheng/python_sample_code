FROM tensorflow/tensorflow:latest-gpu-py3-jupyter AS pre

WORKDIR /repo
RUN apt-get -qqy update && apt-get install -qqy \
    curl \
    npm \
    nodejs

FROM pre AS dev
# COPY ./* /repo
RUN pip install --upgrade pip && pip install \
    pandas \
    scipy \
    scikit-learn \
    matplotlib \
    seaborn \
    jupyterlab
# pip install -r requirements.txt
RUN jupyter labextension install @jupyterlab/toc
RUN chmod -R 777 /.local ~/.jupyter