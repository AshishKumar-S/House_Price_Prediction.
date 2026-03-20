# Use official Python 3.11 slim image as base
FROM python:3.11-slim

# set working directory inside container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Copy the joblib
COPY california1.joblib .

# Copy all project files into container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port FastAPI will run on
EXPOSE 8000

# command to run FastAPI with uvicorn
# CMD ["uvicorn", "california_app:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["uvicorn", "california_app:app", "--host", "0.0.0.0", "--port", "8000"]