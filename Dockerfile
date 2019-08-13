FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN pip -V

RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel

RUN apt-get install -y libsm6 libxext6 libxrender-dev

COPY app /src/app

WORKDIR /src/app

COPY requirements.txt /src/requirements.txt

RUN pip -V
RUN pip install pyserial
RUN pip install -r /src/requirements.txt

CMD gunicorn --bind 0.0.0.0:$PORT app:app --timeout 240
