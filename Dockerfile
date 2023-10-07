FROM python:3.10-rc-slim

ENV PIPENV_VERBOSITY -1

RUN apt-get update

RUN pip install pipenv

RUN mkdir /pellets

WORKDIR /pellets

COPY ./src ./src ./\
COPY ./commands ./commands
COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy

CMD ["bash"]

