# syntax = docker/dockerfile:1.0-experimental
# DOCKER_BUILDKIT=1 docker build . -f recommendations/Dockerfile \
#                     -t recommendations --secret id=ca.key,src=ca.key

FROM python

# Set the working directory to /app
RUN mkdir /service

COPY protobufs/ /service/protobufs/

COPY recommendations/ /service/recommendations/

WORKDIR /service/recommendations

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt


ENTRYPOINT ["python", "main.py"]
