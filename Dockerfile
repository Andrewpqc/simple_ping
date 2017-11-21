FROM debian:latest
COPY . /app
RUN apt-get update \ 
&& apt-get install -y python3-pip python3-dev python3.5 python-dev  \
&& pip3 install --upgrade pip \
&& pip3 install -r requirements.txt \
&& apt-get autoremove
CMD [ "/usr/bin/python3","/app/SimplePing/manage.py","runserver","-h","0.0.0.0","-p","9999" ]
EXPOSE 9999
