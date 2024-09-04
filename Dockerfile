# Use the official Python image as a base
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
# RUN echo "192.168.29.239 DarkLord" >> /etc/hosts 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /app/

# Run migrations
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# Expose the port the Django app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
