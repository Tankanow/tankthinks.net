FROM java:8

RUN apt-get update
RUN apt-get upgrade -y

# AWS cli and git for deployment
RUN apt-get -y install python-setuptools git wget
RUN easy_install awscli awsebcli

# lein
RUN wget -O /usr/local/bin/lein \
      https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
RUN chmod a+x /usr/local/bin/lein

## Application Commands
# Rename this to your application name
ENV APPLICATION tankthinks.net
ENV APP_PORT 3000
WORKDIR /opt/tankthinks/${APPLICATION}

COPY . ./

# ENTRYPOINT ["cicd/run.sh"]
# CMD ["run"]
