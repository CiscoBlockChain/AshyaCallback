FROM python:3-alpine
#RUN apk add build-base
RUN apk update \
    && apk upgrade \
    && apk add --update make gcc python3-dev musl-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt
ADD simple.py /app/
WORKDIR /app
EXPOSE 5252
CMD [ "python3", "simple.py" ]
