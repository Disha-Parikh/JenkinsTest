#!/bin/bash
if [ -x "$(command -v docker)" ]; then
    echo "Docker Installed!"
else
	/bin/bash /home/JenkinsTest/istall_docker.sh
    # command
fi
sudo apt-get install nginx -y
cd JenkinsTest
pwd
sudo docker-compose up -d
echo "SERVICES"
sudo docker-compose ps --services
echo "LOGS WEB"
sudo docker-compose logs web
echo "LOGS DB"
sudo docker-compose logs postgres
echo "RESTART"
sudo netstat -tnlp
sudo docker-compose stop web
sudo docker-compose start web
echo "post"
sudo docker-compose logs web
sudo netstat -tnlps
echo "NETWORKS"
sudo docker network ls
echo "END it well"
curl localhost:5002
sudo touch /etc/systemd/system/app.service
# #sudo ss -lptn 'sport = :5002' | awk 'match($0,/[=]+[0-9]+/) {print substr($0,RSTART,RLENGTH)}'
# =8665
