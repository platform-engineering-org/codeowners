FROM mcr.microsoft.com/vscode/devcontainers/python:3.12@sha256:a067e746fb8291fac357e5fbae6f68f1e34e44cfa9d318656ee9d1708ce9d464

WORKDIR /usr/local/share/ca-certificates
RUN curl -s --fail https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem -o /usr/local/share/ca-certificates/Current-IT-Root-CAs.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

WORKDIR /source
COPY requirements.txt ./
RUN pip install -r requirements.txt
