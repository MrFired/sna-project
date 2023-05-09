FROM python:3.10.5-slim-buster

COPY Pipfile /app/
COPY Pipfile.lock /app/
WORKDIR /app
RUN pip3 install pipenv && pipenv install --deploy --clear --system;
COPY .env /app/

COPY src ./src
EXPOSE 5000
ENTRYPOINT [ "python", "-m", "src.web" ]