FROM golang:1.20rc1-alpine3.17

RUN addgroup app && adduser -S -G app app
USER app

ENV HOME /go/github.com/RYLiang18/venmoscription-backend
RUN mkdir -p ${HOME}

WORKDIR ${HOME}