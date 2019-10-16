FROM python:3.5

RUN apt-get update
RUN apt-get install -y python3-dev python3-pip
RUN apt-get install -y libffi6
RUN apt-get install -y libffi-dev
RUN apt-get install -y build-essential
RUN pip install flask flask_sqlalchemy psycopg2-binary
WORKDIR .
COPY . .
EXPOSE 5000
EXPOSE 15432
ENTRYPOINT ["python3","/var/lib/jenkins/workspace/myproject_pipeline/Example/app.py"]


