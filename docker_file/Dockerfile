FROM selenium:latest

RUN sudo apt-get update
RUN sudo apt-get -y upgrade
RUN sudo apt-get -y install mc git python3-pip
RUN sudo mkdir /home/seluser/Project
WORKDIR /home/seleuser/Project
RUN sudo git clone https://github.com/WolfGung/Otus.git
RUN sudo apt-get -y install python3-pytest
RUN sudo apt-get -y install python3-pip
RUN sudo pip3 install allure-pytest
RUN export PYTHONPATH="$PYTHONPATH:/home/seluser/Project/Otus"
