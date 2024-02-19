FROM mcr.microsoft.com/vscode/devcontainers/python:3.12@sha256:672331fb5736373404e965211a877fdabda822c3d93b85fc90ed00165241b556

WORKDIR /usr/local/share/ca-certificates
RUN curl -s --fail https://certs.corp.redhat.com/certs/Current-IT-Root-CAs.pem -o /usr/local/share/ca-certificates/Current-IT-Root-CAs.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

WORKDIR /source
COPY requirements.txt ./
RUN pip install -r requirements.txt
