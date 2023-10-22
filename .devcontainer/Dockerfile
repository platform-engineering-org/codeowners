FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

WORKDIR /usr/local/share/ca-certificates
RUN curl -skO https://certs.corp.redhat.com/certs/Current-IT-Root-CA.pem && \
    chmod 644 Current-IT-Root-CA.pem && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/usr/local/share/ca-certificates/Current-IT-Root-CA.pem

WORKDIR /source
COPY requirements.txt ./
RUN pip install -r requirements.txt
