sudo rm file_storage/*
sudo docker kill $(docker -q)
sudo docker rm $(docker -aq)