FROM python:3.8

RUN python3.8 -m pip install --upgrade pip
 
WORKDIR /app

ADD requirements.txt .

RUN python3.8 -m pip install -r requirements.txt --no-cache-dir

COPY . /app/

ENTRYPOINT [ "gunicorn" ]

CMD ["-w", "2", "-b", "0.0.0.0:5005", "wsgi:app"]
