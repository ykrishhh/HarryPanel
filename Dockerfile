FROM python:3.11-slim

WORKDIR /app

# Copy requirements first for better caching
COPY harry-backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY harry-backend/ ./harry-backend/

# Expose port
EXPOSE 5000

# Set environment
ENV PORT=5000

# Run with gunicorn
WORKDIR /app/harry-backend
CMD ["gunicorn", "app:app", "--worker-class", "eventlet", "-w", "1", "--bind", "0.0.0.0:5000"]
