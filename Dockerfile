# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Install necessary tools to add user/group
RUN apt-get update && apt-get install -y --no-install-recommends \
    adduser \
    && rm -rf /var/lib/apt/lists/*

# Create a new group and user with UID and GID 10016
RUN addgroup --gid 10016 choreo && \
    adduser --disabled-password --gecos "" --uid 10016 --gid 10016 --no-create-home choreouser

# Set working directory
WORKDIR /app

# Copy the application code
COPY . .

# Give ownership of /app to the non-root user
RUN chown -R choreouser:choreo /app

# Switch to the new user
USER choreouser

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
