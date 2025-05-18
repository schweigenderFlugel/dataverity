FROM python:3.13-alpine3.21

WORKDIR /api

COPY requirements.txt ./

RUN pip install --no-cache-dir -r ./requirements.txt

COPY api ./

RUN addgroup -g 1234 dataverity-group && \
  adduser -D -u 1234 -G dataverity-group dataverity-user

USER dataverity-user:dataverity-group

CMD ["python", "main.py"]