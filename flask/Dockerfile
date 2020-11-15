FROM alpine:3.2
MAINTAINER Tom Halligan

RUN apk add --update wget && rm -rf /var/cache/apk/*

ENV HUGO_VERSION 0.76.3
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit


WORKDIR /tmp

RUN wget --no-check-certificate https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz \
    && tar -xzf ${HUGO_BINARY}.tar.gz \ 
    && mv hugo /usr/local/bin/hugo \
    && rm -rf /tmp/*

RUN mkdir -p /srv/hugo
COPY . /srv/hugo

WORKDIR /srv/hugo
EXPOSE 1313
CMD ["hugo", "server", "--watch"]
