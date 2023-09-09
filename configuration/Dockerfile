FROM python:3.10

RUN pip3 install poetry --no-cache-dir

RUN mkdir /app
WORKDIR /app
ADD src src
ADD pyproject.toml pyproject.toml
ADD data/data-5-structure-1.csv import-data.csv

RUN poetry install --no-root --without dev

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.12.0/wait /wait
RUN chmod +x /wait

ADD configuration/run.sh run.sh
RUN chmod +x run.sh

EXPOSE 8080

CMD /wait && ./run.sh
