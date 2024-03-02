from python:3.11

RUN pip install poetry

WORKDIR /app



COPY . /app

RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "uvicorn", "main:app","--host", "0.0.0.0", "--port", "8080"]



