FROM nousresearch/hermes-agent:latest

USER root

# Install basic network utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY web_health.py /app/web_health.py
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh /app/web_health.py

EXPOSE 8080

ENV PORT=8080
ENV HERMES_HOME=/root/.hermes

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
