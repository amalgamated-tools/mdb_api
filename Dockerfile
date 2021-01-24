# set base image (host OS)
FROM python:3.8

EXPOSE 80

COPY ./app /app

RUN pip3 install imdbpie fastapi uvicorn JustWatch

RUN apt-get update \
  && apt-get install -y --no-install-recommends git \
  && apt-get purge -y --auto-remove \
  && rm -rf /var/lib/apt/lists/*

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8013"]
