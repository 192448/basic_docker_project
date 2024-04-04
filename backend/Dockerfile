FROM python:alpine3.19

WORKDIR /usr/app

COPY app.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5000","app:app"]
