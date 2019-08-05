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

COPY requirements.txt /src/requirements.txt

RUN pip -V
RUN pip install pyserial
RUN pip install -r /src/requirements.txt

COPY app.py /src
COPY ImageNet /src/ImageNet
COPY static /src/static
COPY templates /src/templates

RUN wget -P /root/.cache/torch/checkpoints/ https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth

CMD python3 /src/app.py

