FROM mcr.microsoft.com/vscode/devcontainers/python:3.12@sha256:d918f8f5b04375ff0ba0af0a5beaad3466a14674eab2f6906441d238392f9dbc

WORKDIR /usr/local/share/ca-certificates
RUN curl -s --fail https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem -o /usr/local/share/ca-certificates/Current-IT-Root-CAs.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

WORKDIR /source
COPY requirements.txt ./
RUN pip install -r requirements.txt
