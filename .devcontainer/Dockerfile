FROM mcr.microsoft.com/vscode/devcontainers/python:3.12@sha256:d79353264c02d921f736cb31a8a1c1a3a1498f2e5e7097c52ddaf1a0a92fb6ec

WORKDIR /usr/local/share/ca-certificates
RUN curl -s --fail https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem -o /usr/local/share/ca-certificates/Current-IT-Root-CAs.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

WORKDIR /source
COPY requirements.txt ./
RUN pip install -r requirements.txt
