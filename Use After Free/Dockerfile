FROM ubuntu:18.04

ENV PATH="${PATH}:/usr/local/lib/python3.6/dist-packages/bin"
ENV LC_CTYPE=C.UTF-8

RUN apt update
RUN apt install -y \
    gcc \
    git \
    python3 \
    python3-pip \
    ruby \
    sudo \
    tmux \
    vim \
    wget

# install pwndbg
WORKDIR /root
RUN git clone https://github.com/pwndbg/pwndbg
WORKDIR /root/pwndbg
RUN git checkout 2023.03.19
RUN ./setup.sh

# install pwntools
RUN pip3 install --upgrade pip
RUN pip3 install pwntools

# install one_gadget command

WORKDIR /root
