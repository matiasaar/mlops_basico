FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ src/
COPY pipeline/ pipeline/

ENTRYPOINT ["python"]
