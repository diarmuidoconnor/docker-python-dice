#publicly available docker image "python" on docker hub will be pulled
FROM python:3.9.19

RUN mkdir -p /code
WORKDIR /code 

COPY script.py /dockerscript.py 

ENV PYTHONUNBUFFERED="0"

CMD python /dockerscript.py
