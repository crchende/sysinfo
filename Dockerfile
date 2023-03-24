FROM python:3.8-alpine

ENV FLASK_APP sysinfo
#ENV FLASK_CONFIG = docker

#3.8 booster
#RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site

#3.8 alpine
RUN adduser -D sysinfo

USER sysinfo

WORKDIR /home/sysinfo/

COPY app app

RUN python -m venv .venv
RUN .venv/bin/pip install -r app/quickrequirements.txt

WORKDIR /home/sysinfo/app

# runtime configuration
EXPOSE 5020
ENTRYPOINT ["./dockerstart.sh"]
#CMD flask run --host 0.0.0.0 -p 5010
