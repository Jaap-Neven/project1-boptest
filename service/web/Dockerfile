FROM ubuntu:focal

RUN apt-get update && apt-get -y install ca-certificates curl build-essential
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - \
    && apt-get install -y nodejs

RUN mkdir /root/server

COPY service/web/server/package.json service/web/server/package-lock.json /root/server/
COPY version.txt /boptest/

WORKDIR /root/server
RUN npm install

WORKDIR /root/server
COPY service/web/server /root/server
RUN npm run build

CMD [ "npm", "start" ]
