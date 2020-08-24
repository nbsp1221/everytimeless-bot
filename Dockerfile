FROM python:3.8
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH=/root/.poetry/bin:$PATH
COPY [ "poetry.lock", "pyproject.toml", "/app/" ]
COPY src/* /app/src/
WORKDIR /app
RUN poetry config virtualenvs.create false && \
    poetry install
CMD [ "python", "src/main.py" ]
