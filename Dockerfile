# pull base image from docker hub
FROM python:3.10-slim

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#copy requirements.txt file from working directory & install dependencies
COPY requirements.txt ./
RUN apt-get update && \
    apt-get install -y build-essential

RUN pip install --no-cache-dir -r requirements.txt


# copy entire project 
COPY . .

# change to the directory containing the Flask app
WORKDIR /usr/src/app/supportbot


# Start Gunicorn
CMD ["uwsgi", "--ini", "supportbot.ini"]