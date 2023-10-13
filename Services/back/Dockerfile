FROM python:3.9-slim


RUN apt-get update && apt-get install -y libgmp-dev libmpc-dev
RUN apt-get update && apt-get install -y build-essential


WORKDIR /app

COPY /API .
COPY /env .
COPY /__pycache__ .
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 8001


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]


