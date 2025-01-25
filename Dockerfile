# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Gunicorn will use
EXPOSE 8080

# Run the Django application using Gunicorn
CMD ["gunicorn", "ytprj.wsgi:application", "--bind", "0.0.0.0:8080"]
