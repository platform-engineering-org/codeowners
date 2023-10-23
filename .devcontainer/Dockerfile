FROM mcr.microsoft.com/vscode/devcontainers/python:3.12@sha256:a0e9fce8db35cc4ca5365e020b5627d7bfe98425cd53c2b0c350879c6dfbaaeb

WORKDIR /usr/local/share/ca-certificates
RUN curl -s --fail https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem -o /usr/local/share/ca-certificates/Current-IT-Root-CAs.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

WORKDIR /source
COPY requirements.txt ./
RUN pip install -r requirements.txt
