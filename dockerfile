# Use a specific Python base image
FROM python

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=DRF_SocialNetwork.settings

# Create and set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . /app/

# Install any required dependencies
RUN pip install -r requirements.txt

# Expose the port that Uvicorn will listen on (adjust as needed)
EXPOSE 8000

# Define the entry point for running Uvicorn with your Django ASGI application
CMD ["uvicorn", "DRF_SocialNetwork.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
