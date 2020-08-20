#!/bin/bash
sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
echo "!!!!!!"
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
cd JenkinsTest
pwd
sudo apt-get install -y nginx
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
sudo cp abcd.txt /etc/systemd/system/app.service
