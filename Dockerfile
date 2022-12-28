FROM golang:1.20rc1-alpine3.17

RUN addgroup app && adduser -S -G app app
USER app

ENV HOME /home/app
RUN mkdir -p ${HOME}

WORKDIR ${HOME}