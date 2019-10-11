FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

RUN apt-get -qqy update && apt-get install -qqy curl npm nodejs
RUN pip install pandas scipy scikit-learn matplotlib seaborn jupyterlab
RUN jupyter labextension install @jupyterlab/toc
RUN chmod -R 777 /.local
#CMD chown -R user:user ~/.local/share/jupyter

# && export CLOUD_SDK_REPO="cloud-sdk-xenial" \
# && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
# && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
# && apt-get -qqy update && apt-get install -qqy google-cloud-sdk \
# && gcloud auth activate-service-account huafeng.sheng@cloud-iq.com --key-file=/home/huafeng/Desktop/Python_Code/authentication_file.json
# here the json file is not in the image built. it is in local system not in docker. need to do sth here.
