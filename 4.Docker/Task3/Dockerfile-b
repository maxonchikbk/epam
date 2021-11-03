FROM ubuntu:20.04
ENV PYTHONUNBUFFERED=1 DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y python3-pip
COPY ./lib_catalog .
RUN pip install -r requirements.txt