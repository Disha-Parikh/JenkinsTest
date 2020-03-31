FROM python:3.5
RUN apt-get update
RUN apt-get install -y python3-dev python3-pip
RUN apt-get install -y libffi6
RUN apt-get install -y libffi-dev
RUN apt-get install -y build-essential
RUN apt-get install -y virtualenv
RUN pip install flask flask_sqlalchemy psycopg2-binary virtualenv gunicorn
WORKDIR .
COPY . .
EXPOSE 5002
EXPOSE 5432
ENTRYPOINT ["python3","app.py"]


