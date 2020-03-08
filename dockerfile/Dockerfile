FROM python:3.8

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV PATH $PATH:/root/.poetry/bin
WORKDIR /host/nayose
COPY startup.sh /startup.sh