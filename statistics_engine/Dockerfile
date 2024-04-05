FROM python:alpine3.19

WORKDIR /usr/statistics

COPY app.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 9000

ENTRYPOINT ["gunicorn","--bind","0.0.0.0:9000","app:app"]
