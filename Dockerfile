# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# 1. Define non‑root UID/GID above 10000 for security & platform compliance
ARG USER_UID=10001
ARG USER_GID=$USER_UID

# 2. Create group and user, adjust permissions
RUN groupadd --gid $USER_GID appgroup \
  && useradd --uid $USER_UID --gid appgroup --shell /bin/bash --create-home appuser \
  && mkdir /app \
  && chown appuser:appgroup /app

# 3. Switch to the non‑root user you just created
USER appuser

# 4. Set the working directory
WORKDIR /app

# 5. Copy the current directory contents into the container at /app
COPY --chown=appuser:appgroup . /app

# 6. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 7. Expose and run
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
