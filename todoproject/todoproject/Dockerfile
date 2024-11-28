# Using official python image
FROM python:3.10-slim

# Setting up working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Copy application files
COPY . .

# Expose port
EXPOSE 8080

# Set up Gunicorn as the production server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todoproject.wsgi:application"]