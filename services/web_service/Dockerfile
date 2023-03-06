FROM node:19.7-alpine AS node

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run css

FROM python:3.10

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

COPY --from=node src/frontend/static/css src/frontend/static/css

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

CMD python3 /src/backend/service.py