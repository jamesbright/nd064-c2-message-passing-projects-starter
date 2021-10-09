FROM node:14.8.0-alpine3.12
RUN mkdir /frontend
WORKDIR /frontend
COPY package.json /frontend/package.json
RUN npm install
RUN npm install react-scripts@3.4.3 -g


