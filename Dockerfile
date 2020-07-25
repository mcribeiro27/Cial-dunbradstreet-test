FROM python:3.6.4-alpine3.7
WORKDIR /app
ADD ./app Users/marcoscesarribeiro/PycharmProjects/Cial/
RUN pip install -r requirements.txt
