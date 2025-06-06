# Use an official Python runtime as a parent image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies for Python and additional tools
RUN apk add --no-cache build-base libffi-dev openssl-dev nodejs npm git dos2unix

# Configure Git to ignore ownership issues in the /app directory
RUN git config --global --add safe.directory /app

# Copy and give execution permission to the entrypoint script
COPY ./docker-entrypoint.sh /app/docker-entrypoint.sh
RUN dos2unix /app/docker-entrypoint.sh && chmod +x /app/docker-entrypoint.sh
RUN dos2unix /app/app/portafolio/tailwind.sh && chmod +x /app/app/portafolio/tailwind.sh

# Copy only the requirements file initially to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt 

# Expose the port on which your Django app will run
EXPOSE 8000

# Set the entrypoint to the docker-entrypoint.sh script
ENTRYPOINT ["sh", "/app/docker-entrypoint.sh"]
