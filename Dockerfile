FROM tensorflow/tensorflow:latest-gpu-py3-jupyter AS pre

WORKDIR /repo
RUN apt-get -qqy update && apt-get install -qqy \
    curl \
    npm \
    nodejs

FROM pre AS dev
COPY ./requirement.txt /repo/
RUN mkdir /.jupyter /.config
RUN pip install --upgrade pip && pip install -r requirement.txt
RUN jupyter labextension install @jupyterlab/toc
RUN chmod -R 777 /.local /.jupyter /.config

CMD ["/bin/bash"]
# need to install vim and set vims... in case of some package problems...
# eg. /usr/local/lib/python3.6/dist-packages/astropy/config/configuration.py:532: ConfigurationMissingWarning: Configuration defaults will be used due to PermissionError:13 on None
#  warn(ConfigurationMissingWarning(msg))


#docker build -t $(basename $("pwd")) .
#
#docker run -it -u $(id -u):$(id -g) \
#               --rm \
#               --network="host" \
#               -v /$(pwd):/repo \
#               -w /repo \
#               --name $(basename $("pwd"))\
#               $(basename $("pwd")):latest \
#               bash