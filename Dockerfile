# # Use a slim version of Python
# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     libffi-dev \
#     libssl-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements
# COPY requirements.txt .

# # Install Rasa SDK and other dependencies
# RUN python3.9 -m venv /app/venv \
#     && /app/venv/bin/pip install --no-cache-dir --upgrade pip \
#     && /app/venv/bin/pip install --no-cache-dir rasa \
#     && /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# # Verify installation
# RUN /app/venv/bin/pip show rasa || (echo "Rasa not installed!" && exit 1)

# # Copy the actions directory
# COPY actions /app/actions

# # Set environment variables
# ENV PATH="/app/venv/bin:/app/venv/Scripts:$PATH"

# # Expose port for the action server
# EXPOSE 5055

# # Command to run the action server
# CMD ["/app/venv/bin/rasa", "run", "actions", "--port", "5055"]


# # Use the official Rasa SDK image for custom actions
# FROM rasa/rasa-sdk:latest

# # Switch to root user to install additional dependencies (if needed)
# USER root

# # Install Rasa (core) and other necessary dependencies
# RUN pip install rasa


# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements file if you have one (optional)
# COPY requirements.txt /app/requirements.txt

# # Install dependencies if you have a requirements.txt (uncomment below line if necessary)
# RUN pip install --no-cache-dir --timeout=300 --retries=5 -r /app/requirements.txt

# # Copy the actions directory into the container
# COPY actions /app/actions

# # Copy the models directory into the container
# COPY models /app/models

# # Optionally copy other parts of the project (e.g., config, domain, etc.)
# COPY . /app

# # Set the entry point to run the action server
# ENTRYPOINT ["rasa", "run", "actions", "--cors", "*"]

# # Use the official Rasa SDK image as the base image
# FROM rasa/rasa-sdk:3.5.0

# # Set environment variables for Spotify and Twilio
# ENV SPOTIPY_CLIENT_ID="3fb1846897864809ac9694b20ae73d8b"
# ENV SPOTIPY_CLIENT_SECRET="8e64d0bf253449d8b655537d01fd02b3"
# ENV SPOTIPY_REDIRECT_URI="http://localhost:3000"
# ENV TWILIO_ACCOUNT_SID="ACb4d775453eb32f7d7cdc218c84fc3eaa"
# ENV TWILIO_AUTH_TOKEN="18c3bb92780c7f9b88729ac17373f9b1"

# # Install additional dependencies
# RUN pip install spotipy twilio

# # Copy actions folder to the app
# COPY ./actions /app/actions

# # Set the working directory
# WORKDIR /app/actions

# # Start the action server
# CMD ["start", "--actions", "action"]


# Use an appropriate base image with Python 3.9
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .

# Create virtual environment and install dependencies
RUN python3.9 -m venv /app/venv \
    && /app/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the actions directory
COPY actions /app/actions

# Set environment variables
ENV PATH="/app/venv/bin:$PATH"

# Expose the default port for the action server
EXPOSE 5055

# Command to run the action server
CMD ["rasa", "run", "actions", "--port", "5055"]
