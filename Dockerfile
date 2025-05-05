FROM python:3.11-slim

# 1. Define non-root UID/GID
ARG USER_UID=10001
ARG USER_GID=$USER_UID

# 2. Create group and user, prepare /app
RUN apt-get update \
    && apt-get install -y --no-install-recommends adduser \
    && groupadd --gid $USER_GID appgroup \
    && useradd --uid $USER_UID --gid appgroup --shell /bin/bash --create-home appuser \
    && mkdir /app \
    && chown appuser:appgroup /app \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 3. Copy requirements and install as root
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your code (and chown so appuser can read/write)
COPY --chown=appuser:appgroup . .

# 5. Switch to non‑root user
USER appuser

EXPOSE 8000

# 6. Launch with uvicorn (now guaranteed installed)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
