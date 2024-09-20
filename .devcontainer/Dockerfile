FROM mcr.microsoft.com/vscode/devcontainers/python:3.12@sha256:b87bec59ee604de9737b6be24a6b26929e52ce2f70a0042058ce92b01584e456

WORKDIR /usr/local/share/ca-certificates
RUN curl -s --fail https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem -o /usr/local/share/ca-certificates/Current-IT-Root-CAs.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

WORKDIR /source
COPY requirements.txt ./
RUN pip install -r requirements.txt
