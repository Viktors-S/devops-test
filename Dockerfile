# Use the Python 3.13 slim image as the base
FROM python:3.13.0a5-slim-bullseye

# Update pip to the latest version
RUN python -m pip install --no-cache-dir --upgrade pip

# Create a directory for your application code
WORKDIR /web

# Copy the current directory contents into the container at /web
COPY . /web

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Set the FLASK_APP environment variable
ENV FLASK_APP=main.py

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
