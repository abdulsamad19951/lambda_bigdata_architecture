FROM python:3.6

RUN apt-get update
RUN apt-get install nano

RUN mkdir api

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
COPY flask_app /api/

WORKDIR /api/
EXPOSE 6007
CMD python app.py



