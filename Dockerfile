FROM python:3.5

RUN apt-get update
RUN apt-get install -y python3-dev python3-pip
RUN apt-get install -y libffi6
RUN apt-get install -y libffi-dev
RUN apt-get install -y build-essential
RUN pip install -r requirements.txt
WORKDIR .
COPY . .
EXPOSE 5000
EXPOSE 15432
ENTRYPOINT ["python3","/Example/app.py"]


