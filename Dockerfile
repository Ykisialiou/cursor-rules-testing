# Multi-stage Dockerfile for pytonator
FROM python:3.11-slim as builder

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim

# Create non-root user
RUN groupadd -r pytonator && useradd -r -g pytonator pytonator

# Set working directory
WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /home/pytonator/.local

# Copy application code
COPY pytonator/ ./pytonator/

# Set environment variables
ENV PATH=/home/pytonator/.local/bin:$PATH
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=pytonator.main

# Change ownership to non-root user
RUN chown -R pytonator:pytonator /app

# Switch to non-root user
USER pytonator

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/time')" || exit 1

# Run the application
CMD ["python", "-m", "pytonator.main"] 