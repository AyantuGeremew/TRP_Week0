# Use a lightweight Python 3.11 image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for MCP and common tools
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Set environment variables
ENV PYTHONPATH=/app
ENV CHIMERA_MODE=GOVERNOR

# Default command: Run tests
CMD ["pytest", "tests/"]