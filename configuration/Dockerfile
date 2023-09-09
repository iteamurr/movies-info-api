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

ENV DEBUG="True"
ENV SECRET_KEY="django-insecure-b8f9=&kxb=qh5sn#hs5j*&6$#=uk@2$t8pr8mtt&06t3uhn$v9"
ENV POSTGRES_DB="movies_info_api_db"
ENV POSTGRES_USER="movies_info_api_db_agent"
ENV POSTGRES_PASSWORD="hackme"
ENV POSTGRES_HOST="localhost"
ENV POSTGRES_PORT="5432"
ENV LOCAL_DB=True

CMD /wait && ./run.sh
