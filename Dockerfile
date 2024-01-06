FROM python:3.10-alpine

ENV FLASK_APP sysinfo
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D sysinfo

USER sysinfo

WORKDIR /home/sysinfo/

COPY app app
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY sysinfo.py sysinfo.py
RUN mkdir static
RUN mkdir static/imagini
RUN chmod -R 777 static

RUN python3 -m venv .venv
RUN .venv/bin/pip install -r quickrequirements.txt

#WORKDIR /home/sysinfo/app

# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart_jenkins.sh"]
#CMD sh
