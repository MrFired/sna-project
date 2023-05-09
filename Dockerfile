FROM python:3.11-slim-buster

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip3 install pipenv && pipenv install --deploy --clear --system;
COPY .env .

COPY src ./src
EXPOSE 5000
ENTRYPOINT [ "python", "-m", "src.web" ]