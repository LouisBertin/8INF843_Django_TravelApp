FROM python:3
RUN apt-get update && apt-get install -f -y postgresql-client
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# Expose ports
EXPOSE 8000

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

# default command to execute
ENTRYPOINT [ "sh", "entrypoint.sh", "db" ]
