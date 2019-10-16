# Python
This repo are collection of generic python samples to quickly refresh memories

## Setting
#### Build up Environment with Docker
```bash
# build docker image for this repo
# -t: tag image as "python_sanmple_code"
# -f: specify a Dockerfile
docker build -t python_sample_code -f Dockerfile.dev . 

# build and set up connection to container for the 1st time 
bash docker_run.sh

# access container after initial setup
docker start -i python_sample_code

# run jupyter in container
jupyter lab --ip=0.0.0.0 --port=8888
```
### Automated Port Mapping 
```bash
basically, need a script to recersively check port availability, and then map
it to available nearest port 
```

## Notebooks
Don't ever clear result of Notebooks! Run all won't work as some cell were supposed to 
be not working as counter examples.

File | Content
------------ | ------------
basic_python.ipynb | Pure Python Knowledge Base. Code in Class part is not optimised
