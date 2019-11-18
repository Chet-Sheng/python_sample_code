FROM python:3.7 as pre

WORKDIR /repo

FROM pre AS base
COPY ./* /repo/
RUN pip install pandas

FROM base AS dev
CMD ["/bin/bash"]

# docker build -t $(basename $("pwd")) .


docker run -it -u $(id -u):$(id -g) \
               --rm \
               --network="host" \
               -v /$(pwd):/repo \
               -w /repo \
               --name $(basename $("pwd"))\
               $(basename $("pwd")):latest \
               bash