FROM selenium/standalone-chrome
CMD echo "now running..."

RUN sudo apt-get update && sudo apt-get install -y fish git vim python3 curl cron
RUN curl -kL https://bootstrap.pypa.io/get-pip.py | sudo python3 
RUN sudo pip install selenium requests

ADD crontab /etc/cron.d/hello-cron
RUN sudo chmod 0644 /etc/cron.d/hello-cron

RUN sudo touch /var/log/cron.log
CMD sudo cron && sudo tail -f /var/log/cron.log
