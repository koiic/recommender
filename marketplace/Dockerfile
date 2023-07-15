
FROM python

LABEL authors="calory"

# Set the working directory to /app
RUN mkdir /service

COPY protobufs/ /service/protobufs/

COPY marketplace/ /service/marketplace/



WORKDIR /service/marketplace

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY marketplace/recommendations_pb2_grpc.py /service/marketplace/recommendations_pb2_grpc.py
EXPOSE 5000

ENV FLASK_APP=marketplace.py

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
