FROM openjdk:11

# Maintainers on this project are the following:
MAINTAINER Abderraouf Bouyahi <abderraouf.bouyahi@gmail.com>

RUN echo "deb https://packages.atlassian.com/atlassian-sdk-deb stable contrib" >>/etc/apt/sources.list \
    && wget https://packages.atlassian.com/api/gpg/key/public  \
    && apt-key add public \
    && apt-get update \
    && apt-get install --yes atlassian-plugin-sdk \
    && mkdir /opt/atlas \
    && cd /opt/atlas


CMD ["atlas-debug"]
