# pull base image from docker hub
FROM python:3.10-slim

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#copy requirements.txt file from working directory & install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy entire project 
COPY . .


# Start Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "supportbot.views:app"]

