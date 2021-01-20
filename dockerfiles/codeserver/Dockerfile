FROM codercom/code-server:3.4.1

USER root

RUN apt-get update

# C++ install
RUN apt-get install -y gcc wget

# Golang install
RUN wget https://dl.google.com/go/go1.12.7.linux-amd64.tar.gz && \
    tar -xvf go1.12.7.linux-amd64.tar.gz && \
    mv go /usr/local
ENV GOROOT /usr/local/go
ENV GOPATH /home/coder/project/go
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH

# Python install
RUN apt-get install -y \
    python3.7 \
    python3-pip &&\
    pip3 install pipenv &&\
    pip3 install pylint

# PHP Install
RUN apt-get install php -y

# Docker Install
COPY ./buildfiles/get-docker.sh .

RUN sh get-docker.sh &&\
    curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose &&\
    chmod +x /usr/local/bin/docker-compose

# zsh and zsh plugins
RUN apt-get install -y zsh &&\
	chsh -s /bin/zsh &&\
    touch /home/coder/.zshrc &&\
    usermod -m -d /home/coder coder

ENV SHELL /usr/bin/zsh

# Other nice things
RUN apt-get install -y neofetch

RUN chown -R coder:coder /home/coder

USER coder

# Install Sharp Programs

RUN sudo curl -s -L https://github.com/Sharpz7/gopack/releases/download/0.1.2/install.sh | sudo bash
RUN sudo curl -s -L https://github.com/Sharpz7/sharpdev/releases/download/0.1.2/install.sh | sudo bash

# Add sharpnet file
COPY ./sharpnet/nginx.conf /sharpnet/nginx.conf


