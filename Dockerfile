FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/app


COPY ./requirements.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/app
RUN python manage.py collectstatic --no-input

EXPOSE 8000
