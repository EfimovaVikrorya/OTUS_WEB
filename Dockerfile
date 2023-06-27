FROM python:3.10-bullseye
RUN apt-get update && apt-get install -y chromium
WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT ["pytest"]