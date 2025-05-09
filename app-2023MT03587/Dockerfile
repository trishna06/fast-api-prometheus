# Use official Python image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy files into the container
COPY main.py .
COPY .env .
COPY requirement.txt .

# Install dependenciesCOPY requirements.txt .
RUN pip install -r requirement.txt

# Expose port 8000
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]