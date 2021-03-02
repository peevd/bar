FROM python:3
ENV PYTHONUNBUFFERED=1


WORKDIR /test_app
COPY requirements.txt /test_app/
RUN pip install -r requirements.txt
COPY . /test_app/
