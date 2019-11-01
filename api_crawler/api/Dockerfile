FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install -y python3-pip python3-dev build-essential
RUN cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
COPY . /api
WORKDIR /api
RUN pip install -r requirements.txt
CMD python -u api.py

