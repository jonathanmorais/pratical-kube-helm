FROM python:3.6

WORKDIR /

RUN pip install flask

COPY app app

CMD [ "python3", "app/main.py" ]