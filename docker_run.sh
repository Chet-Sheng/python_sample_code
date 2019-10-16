docker run -it -u $(id -u):$(id -g) \
               -p 8888:8888 \
               -p 6006:6006 \
               -v /$(pwd):/repo \
               -w /repo \
               --name $(basename $("pwd"))\
               python_sample_code:latest \
               bash
