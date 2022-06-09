FROM ubuntu:18.04
LABEL Maintainer: Ryan Pisani <rpisani@5thcolumn.net>

ARG CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apt-get update && apt-get -y install python3-pip dpkg-dev fakeroot lintian
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

COPY build-pkg.py /build-pkg.py

CMD /usr/bin/python3 /build-pkg.py